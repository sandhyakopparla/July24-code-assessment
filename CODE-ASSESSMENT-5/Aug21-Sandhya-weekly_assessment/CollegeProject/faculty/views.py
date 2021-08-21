from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
import json
from faculty.serializers import facultySerializer
from faculty.models import Faculty
from rest_framework.parsers import JSONParser 
from rest_framework import status
@csrf_exempt
def facultyPage(request):
    if(request.method=="POST"):
       mydict=JSONParser().parse(request)   
       faculty_serialize=facultySerializer(data=mydict)  
       if(faculty_serialize.is_valid()):
           faculty_serialize.save()
           return JsonResponse(faculty_serialize.data,status=status.HTTP_200_OK)
       else:
           return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return Httpresponse("No Get method allowed",status=status.HTTP_400_BAD-REQUEST)
@csrf_exempt
def faculty_list(request):
    if(request.method=="GET"):
        faculty=Faculty.objects.all()
        faculty_serializer=facultySerializer(faculty,many=True)
        return JsonResponse(faculty_serializer.data,safe=False)
@csrf_exempt
def faculty_details(request,fetchid):
    try:
        faculty=Faculty.objects.get(id=fetchid)
        if(request.method=="GET"):
            faculty_serializer=facultySerializer(faculty)
            return JsonResponse(faculty_serializer.data,safe=False,status=status.HTTP_200_OK)
        if (request.method=="DELETE"):
            faculty.delete()
            return HttpResponse("Deleted",status=status.HTTP_200_OK)
        if (request.method=="PUT"):
            mydict=JSONParser().parse(request)
            faculty_serializer=facultySerializer(faculty,data=mydict)
            if(faculty_serializer.is_valid()):
                faculty_serializer.save()
                return JsonResponse(faculty_serializer.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(faculty_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except Faculty.DoesNotExist:
        return HttpResponse("invalid faculty id",status=status.HTTP_404_NOT_FOUND)
@csrf_exempt
def faculty_search(request,fetchfaculty_code):
    try:
        faculty=Faculty.objects.get(faculty_code=fetchfaculty_code)
        if(request.method=="GET"):
            faculty_serializer=facultySerializer(faculty)
            return JsonResponse(faculty_serializer.data,safe=False,status=status.HTTP_200_OK)
    except Faculty.DoesNotExist:
        return HttpResponse("invalid faculty code",status=status.HTTP_404_NOT_FOUND)
def facultyregister_view(request):
    return render(request,'facultyregister.html')
def facultylogin_view(request):
    return render(request,'facultylogin.html')
