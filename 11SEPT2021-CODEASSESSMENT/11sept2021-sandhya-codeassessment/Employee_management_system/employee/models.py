from django.db import models
class Employee(models.Model):
   
    employee_code=models.IntegerField()
    name=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    mobile_no=models.BigIntegerField()
    pincode=models.IntegerField()
    salary=models.CharField(max_length=200)
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)

