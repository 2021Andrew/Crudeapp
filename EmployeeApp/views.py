from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from EmployeeApp.models import Department, Employee
from EmployeeApp.serializers import DepartmentSerializer, EmployeeSerializer

@csrf_exempt
def departmentApi(request, id=0):
    if request.method == "GET":
        departments = Department.objects.all()
        department_serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(department_serializer.data, safe=False)
    elif request.method == "POST":
        department_data = JSONParser().parse(request)
        department_serializer = DepartmentSerializer(data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Added successfully", safe=False)
        ##return JsonResponse("Failed to add", safe=False)
        return JsonResponse(department_serializer.errors, status=400)

    elif request.method == 'PUT':
        department_id = JSONParser().parse(request)
        try:
                department = Department.objects.get(DepartmentId=department_id)
            ##department = Department.objects.get(DepartmentId=department_data['DepartmentId'])
        except Department.DoesNotExist:
            return JsonResponse("Department not found", status=404, safe=False)

        department_serializer = DepartmentSerializer(department, data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Updated successfully", safe=False)
        return JsonResponse("Failed to update", safe=False)
    elif request.method == "DELETE":
        try:
            department = Department.objects.get(DepartmentId=id)
            department.delete()
            return JsonResponse("Deleted successfully", safe=False)
        except Department.DoesNotExist:
            return JsonResponse("Department not found", status=404, safe=False)
        ## crud operation for employee model

@csrf_exempt
def employeeApi(request, id=0):
    if request.method == "GET":
        employees = Employee.objects.all()
        employee_serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(employee_serializer.data, safe=False)
    elif request.method == "POST":
        employee_data = JSONParser().parse(request)
        employee_serializer = DepartmentSerializer(data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Added successfully", safe=False)
        ##return JsonResponse("Failed to add", safe=False)
        return JsonResponse(employee_serializer.errors, status=400)

    elif request.method == 'PUT':
        employee_id = JSONParser().parse(request)
        try:
                employee = Employee.objects.get(EmployeeId=employee_id)
            ##department = Department.objects.get(DepartmentId=department_data['DepartmentId'])
        except Employee.DoesNotExist:
            return JsonResponse("Employee not found", status=404, safe=False)

        employee_serializer = EmployeeSerializer(employee, data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Updated successfully", safe=False)
        return JsonResponse("Failed to update", safe=False)
    elif request.method == "DELETE":
        try:
            employee = Employee.objects.get(EmployeeId=id)
            employee.delete()
            return JsonResponse("Deleted successfully", safe=False)
        except Department.DoesNotExist:
            return JsonResponse("employee not found", status=404, safe=False)

