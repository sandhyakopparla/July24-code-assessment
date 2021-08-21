from rest_framework import serializers
from student.models import Student
class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=("name","admission_number","roll_number","college","parent_name")

