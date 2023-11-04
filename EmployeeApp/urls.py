from django.urls import path
from . import views

urlpatterns = [
    path('departments/', views.departmentApi, name='department_list'),  # For GET (list) operation
    path('departments/<int:id>/', views.departmentApi, name='department_detail'),  # For GET (detail) operation
    path('departments/create/', views.departmentApi, name='department_create'),  # For POST operation
    path('departments/<int:id>/', views.departmentApi, name='department_update'),  # For PUT operation
    path('departments/<int:id>/', views.departmentApi, name='department_delete'), 
    ## crud operations for Employee table
    path('employee/', views.employeeApi, name='department_list'),  # For GET (list) operation
    path('employee/<int:id>/', views.employeeApi, name='department_detail'),  # For GET (detail) operation
    path('employee/create/', views.employeeApi, name='department_create'),  # For POST operation
    path('employee/<int:id>/', views.employeeApi, name='department_update'),  # For PUT operation
    path('employee/<int:id>/', views.employeeApi, name='department_delete'), # For DELETE operation
]
