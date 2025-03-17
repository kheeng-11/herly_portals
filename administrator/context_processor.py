from .models import *

def sidebar_data(request):
    sections = section.objects.all()
    return {"sections": sections}