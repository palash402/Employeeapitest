from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.db.models.deletion import CASCADE
# Create your models here.


class Department(models.Model):
    Dept_Name = models.CharField(max_length=100)
    Dept_Id = models.IntegerField()


class Employee(models.Model):
    Emp_Id = models.IntegerField(null=True)
    First_Name = models.CharField(max_length=30)
    Last_Name = models.CharField(max_length=30)
    DOB = models.DateField()
    DOJ = models.DateField()
    Address = models.CharField(max_length=200)
    MOb_No = models.CharField(max_length=20)
    Designation = models.CharField(max_length=100)
    Dept_Id = models.ForeignKey(Department, on_delete=models.CASCADE,null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    role_id = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
