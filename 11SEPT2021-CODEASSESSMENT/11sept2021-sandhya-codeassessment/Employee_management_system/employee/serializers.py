from rest_framework import serializers
from employee.models import Employee


class employeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields=('id','employee_code','name','address','mobile_no','pincode','salary','username','password')


        

