from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
@csrf_exempt 
def facultyPage(request):
    if(request.method=="POST"):
        getName=request.POST.get("name")
        getAddress=request.POST.get("address")
        getDepartment=request.POST.get("department")
        getCollege=request.POST.get("college")
        mydict={"name":getName,"address":getAddress,"department":getDepartment,"college":getCollege}
        result=json.dumps(mydict)
        return HttpResponse(result)
    else:
        return Httpresponse("No Get method allowed") 



# Create your views here.
