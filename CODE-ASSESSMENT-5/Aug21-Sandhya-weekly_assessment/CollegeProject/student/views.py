from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
import json
from student.serializers import studentSerializer
from student.models import Student
from rest_framework.parsers import JSONParser 
from rest_framework import status
@csrf_exempt
def studentPage(request):
    if(request.method=="POST"):
       mydict=JSONParser().parse(request)   
       student_serialize=studentSerializer(data=mydict)  
       if(student_serialize.is_valid()):
           student_serialize.save()
           return JsonResponse(student_serialize.data,status=status.HTTP_200_OK)
       else:
           return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return Httpresponse("No Get method allowed",status=status.HTTP_400_BAD-REQUEST)
@csrf_exempt
def student_list(request):
    if(request.method=="GET"):
        student=Student.objects.all()
        student_serializer=studentSerializer(student,many=True)
        return JsonResponse(student_serializer.data,safe=False)
@csrf_exempt
def student_details(request,fetchid):
    try:
        student=Student.objects.get(id=fetchid)
        if(request.method=="GET"):
            student_serializer=studentSerializer(student)
            return JsonResponse(student_serializer.data,safe=False,status=status.HTTP_200_OK)
        if (request.method=="DELETE"):
            student.delete()
            return HttpResponse("Deleted",status=status.HTTP_200_OK)
        if (request.method=="PUT"):
            mydict=JSONParser().parse(request)
            student_serializer=studentSerializer(student,data=mydict)
            if(student_serializer.is_valid()):
                student_serializer.save()
                return JsonResponse(student_serializer.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(student_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except Student.DoesNotExist:
        return HttpResponse("invalid student id",status=status.HTTP_404_NOT_FOUND)
def student_search(request,fetchadmission_number):
    try:
        student=Student.objects.get(admission_number=fetchadmission_number)
        if(request.method=="GET"):
            student_serializer=studentSerializer(student)
            return JsonResponse(student_serializer.data,safe=False,status=status.HTTP_200_OK)
    except Student.DoesNotExist:
        return HttpResponse("invalid admission number",status=status.HTTP_404_NOT_FOUND)
def studentregister_view(request):
    return render(request,'studentregister.html')
