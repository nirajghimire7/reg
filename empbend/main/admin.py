from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['full_name','address','phone','email']


admin.site.register(Employee,EmployeeAdmin)

