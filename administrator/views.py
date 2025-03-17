from django.shortcuts import render, redirect, get_object_or_404
from .models import * 
from django.contrib import messages
from django.contrib.auth.hashers import check_password 
from django.utils.timezone import now
from django.utils.html import escape
from django.urls import reverse
import html

def home(request):
    return render(request, 'administrator/index.html')

def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        try:
            admin_user = admin.objects.get(admin_usermail=email) 
            if check_password(password, admin_user.admin_password):
                request.session["admin_id"] = admin_user.id 
                request.session["admin_email"] = admin_user.admin_usermail  
                return redirect('administrator:home') 
            else:
                messages.error(request, "Incorrect password")
        except admin.DoesNotExist:
            messages.error(request, "Incorrect email")

    return render(request, "administrator/login.html")  

def manage_sections(request):
    section_list = section.objects.all()
    return render(request, 'administrator/manage_sections.html',{"sections": section_list})

def add_section(request):
    if request.method == "POST":
        section_name = escape(request.POST['section_name'])
        setion_check = section.objects.filter(section_name=section_name)
        if setion_check.exists():
            messages.error(request, "Section Name Already exist!")
        else:
            insert_section  = section(
                section_name = section_name,
                section_added_on = now().date(),
                )
            insert_section.save()
            messages.success(request, "Section Added Successfully!")
            
    return render(request, 'administrator/add_section.html')

def delete_section(request,id):
    section_detail = get_object_or_404(section, id=id)
    section_detail.delete()
    return redirect('administrator:manage_sections')

def edit_section(request,id):
    get_section_edit = get_object_or_404(section, id=id)
    if request.method == "POST":
        section_name = escape(request.POST["section_name"])
        if section.objects.filter(section_name=section_name).exclude(id=id).exists():
            messages.error(request, "Section Name Already exist!")
            return redirect(reverse("administrator:edit_section", args=[id]))
        else:
            get_section_edit.section_name = section_name
            get_section_edit.save()
            messages.success(request, "Section details updated successfully!")
            return redirect(reverse("administrator:edit_section", args=[id]))

    return render(request, "edit_section.html", {"section": get_section_edit})

