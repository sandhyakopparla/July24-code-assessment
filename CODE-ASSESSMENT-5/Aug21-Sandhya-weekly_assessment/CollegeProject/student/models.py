from django.db import models
class Student(models.Model):
    name=models.CharField(max_length=50)
    admission_number=models.CharField(max_length=50)
    roll_number=models.CharField(max_length=50)
    college=models.CharField(max_length=50)
    parent_name=models.CharField(max_length=50)
    

