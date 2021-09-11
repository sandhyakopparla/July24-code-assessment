from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
import json
from employee.serializers import employeeSerializer
from employee.models import Employee
from rest_framework.parsers import JSONParser 
from rest_framework import status
import requests

@csrf_exempt
def employeePage(request):
    if(request.method=="POST"):
    #    mydict=JSONParser().parse(request)   
       employee_serialize=employeeSerializer(data=request.POST)  
       if(employee_serialize.is_valid()):
           employee_serialize.save()
           return redirect(viewall)
       else:
           return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("No Get method allowed",status=status.HTTP_400_BAD_REQUEST)

def register(request):
    return render(request,'register.html')

@csrf_exempt
def employee_details(request,fetchid):
    try:
        employee=Employee.objects.get(id=fetchid)
        if(request.method=="GET"):
            employee_serializer=employeeSerializer(employee)
            return JsonResponse(employee_serializer.data,safe=False,status=status.HTTP_200_OK)
        if(request.method=="DELETE"):
            employee.delete()
            return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)
        if(request.method=="PUT"):
            mydata=JSONParser().parse(request)
            employee_serialize=employeeSerializer(employee,data=mydata)
            if(employee_serialize.is_valid()):
                employee_serialize.save()
                return JsonResponse(employee_serialize.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(employee_serialize.errors,status=status.HTTP_400_BAD_REQUEST)    
    except Employee.DoesNotExist:
        return HttpResponse("Invalid ID ",status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def update_data_read(request):
    getId=request.POST.get("newid")

    getemployeecode=request.POST.get("newemployeecode")    
    getname=request.POST.get("newname")
    getaddress=request.POST.get("newaddress")
    getmobileno=request.POST.get("newmobileno")
    getpincode=request.POST.get("newpincode")
    getsalary=request.POST.get("newsalary")
    getusername=request.POST.get("newusername")
    getpassword=request.POST.get("newpassword")
   
    
    mydata={'employee_code':getemployeecode,'name':getname,'address':getaddress,'mobile_no':getmobileno,'pincode':getpincode,'salary':getsalary,'username':getusername,'password':getpassword}
    jsondata=json.dumps(mydata)
    ApiLink="http://127.0.0.1:8000/employee/viewemployee/" + getId
    requests.put(ApiLink,data=jsondata)
    return redirect(viewall)

@csrf_exempt
def update_search_api(request):
    try:
        getemployeecode=request.POST.get("employee_code")
        getemployeecodes=Employee.objects.filter(employee_code=getemployeecode)
        employee_serialize=employeeSerializer(getemployeecodes,many=True)
        return render(request,"update.html",{"data":employee_serialize.data})
    except:   
        return HttpResponse("Invalid employee code",status=status.HTTP_404_NOT_FOUND)

def update(request):
    return render(request,'update.html') 
def home(request):
    return render(request,'home.html')
def header(request):
    return render(request,'header.html')
def login(request):
    return render(request,'login.html')

@csrf_exempt
def employee_list(request):
    if(request.method=="GET"):
        employee=Employee.objects.all()
        employee_serializer=employeeSerializer(employee,many=True)
        return JsonResponse(employee_serializer.data,safe=False)
    
@csrf_exempt

def login_check(request):
    username=request.POST.get("username")
    password=request.POST.get("password")
    getemployee=Employee.objects.filter(username=username,password=password)
    employee_serializer=employeeSerializer(getemployee,many=True)
    if(employee_serializer.data):
        for i in employee_serializer.data:
            x=i["name"]
            y=i["id"]
            print(x)
        request.session['uname']=x
        request.session['uid']=y
        return render(request,'view.html',{"data":employee_serializer.data})
    else:
        return HttpResponse("Invalid Credentials")              

def viewall(request): 
    fetchdata=requests.get("http://127.0.0.1:8000/employee/viewall").json()
    return render(request,'view.html',{"data":fetchdata})