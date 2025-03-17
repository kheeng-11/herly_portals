from django.urls import path
from .views import *

app_name = 'administrator'

urlpatterns = [
	path('',home,name='home'),
	path('login/',login,name='login'),
	path('manage_sections/', manage_sections, name='manage_sections'),
	path('add_section/', add_section, name='add_section'),
	path('delete_section/<int:id>/', delete_section, name='delete_section'),
	path('edit_section/<int:id>/', edit_section, name='edit_section'),
]