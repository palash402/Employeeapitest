from django.db import models

# Create your models here.
class EmpSalary(models.Model):
    Emp_Id=models.IntegerField
    Salary_Month=models.CharField(max_length=30)
    Basic_Salary=models.FloatField()
    TA=models.FloatField()
    DA=models.FloatField()
    PF=models.FloatField()
    Deductions=models.FloatField()
    Convinience=models.FloatField()
    Total_Salary=models.FloatField()
    Net_Salary=models.FloatField()
    Salary_Date=models.DateField()