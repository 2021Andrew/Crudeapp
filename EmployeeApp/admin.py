from django.contrib import admin
from .models import Department, Employee

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('DepartmentId', 'DepartmentName')

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('EmployeeId', 'EmployeeName', 'Department', 'DateOfJoining', 'PhotoFileName')
    list_filter = ('Department', 'DateOfJoining')
    search_fields = ('EmployeeName', 'Department__DepartmentName')  # Allows searching by EmployeeName and DepartmentName

admin.site.register(Department, DepartmentAdmin)
admin.site.register(Employee, EmployeeAdmin)
