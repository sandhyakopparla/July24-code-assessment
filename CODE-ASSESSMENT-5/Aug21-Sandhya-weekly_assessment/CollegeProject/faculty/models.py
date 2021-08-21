from django.db import models
class Faculty(models.Model):
    faculty_code=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    department=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    mobile_number=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)