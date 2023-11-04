from django.db import models

class Department(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=200)

    def __str__(self):
        return self.DepartmentName

class Employee(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=200)
    Department = models.ForeignKey(Department, on_delete=models.CASCADE)
    DateOfJoining = models.DateField()
    PhotoFileName = models.CharField(max_length=200)

    def __str__(self):
        return self.EmployeeName
