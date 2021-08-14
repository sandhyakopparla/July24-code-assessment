# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
@csrf_exempt 
def studentPage(request):
    if(request.method=="POST"):
        getName=request.POST.get("name")
        getAdmissionnumber=request.POST.get("admission_number")
        getRollno=request.POST.get("rollno")
        getCollege=request.POST.get("college")
        getParentName=request.POST.get("parentname")
        mydict={"name":getName,"admission_number":getAdmissionnumber,"rollno":getRollno,"college":getCollege,"parentname":getParentName}
        result=json.dumps(mydict)
        return HttpResponse(result)
    else:
        return Httpresponse("No Get method allowed") 

