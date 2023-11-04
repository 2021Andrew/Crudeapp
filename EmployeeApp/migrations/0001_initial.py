# Generated by Django 4.2.6 on 2023-10-28 23:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('DepartmentId', models.AutoField(primary_key=True, serialize=False)),
                ('DepartmentName', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('EmployeeId', models.AutoField(primary_key=True, serialize=False)),
                ('EmployeeName', models.CharField(max_length=200)),
                ('DateOfJoining', models.DateField()),
                ('PhotoFileName', models.CharField(max_length=200)),
                ('Department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EmployeeApp.department')),
            ],
        ),
    ]