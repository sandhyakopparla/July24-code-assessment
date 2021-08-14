import re,logging,pymongo,smtplib
import updatemodule
import countmodule
from valimodule import validation_of_donor
donarlist=[]
client=pymongo.MongoClient("mongodb://localhost:27017/")
mydatabase=client['DonarsDb']
collection_name=mydatabase['donars']
try:
    class Donars():
        def adddonarDetails(self):
            dict={"name":name,"address":address,"bloodgroup":bloodgroup,"pincode":pincode,"mobile_number":mobile_number,"last_donated_date":last_donated_date,"place":place,"emailid":emailid,"delflag":0}
            donarlist.append(dict)
    obj1=Donars()
    while(True):
        print("\n enter your choice:")
        print("1.Add Donars")
        print("2.view details")
        print("3.Search donars based on blood group")
        print("4.Search donars based on bloodgroup and place:")
        print("5.update all the donar details with their mobile number")
        print("6.delete donar details using mobile number")
        print("7.display the total number of donars count")
        print("8.send the mail")
        print("9.Exit") 
        choice=int(input("enter the choice"))
        if choice==1:
            name=input("enter the name")
            address=input("enter the address")
            bloodgroup=input("enter the bloodgroup")
            pincode=input("enter the pincode")
            mobile_number=input("enter the mobile_number")
            last_donated_date=input("enter the last_donated_date")
            place=input("enter the place")
            emailid=input("enter the emailid")
            if validation_of_donor(name,address,bloodgroup,pincode,mobile_number,place,emailid):
                obj1.adddonarDetails()
                result=collection_name.insert_many(donarlist)
                print(result.inserted_ids)
        if choice==2:
            result=collection_name.find({"delflag":0},{"_id":0})
            for i in result:
                print(i)
                donarlist.clear()
        if choice==3:
            blood_gr=input("enter the blood group to search:")
            result=collection_name.find({"bloodgroup":blood_gr})
            for i in result:
                print(i)
        if choice==4:
            b=input("enter the bloodgroup")
            p=input("enter the place")
            result=collection_name.find({"$and":[{"bloodgroup":b},{"place":p},{"delflag":0}]})
            for i in result:
                print(i)
        if choice==5:
            updatemodule.updatedetails()
        if choice==6:
            mobile=input("enter the mobileno to del")
            result=collection_name.update_one({"mobile_number":mobile},{"$set":{"delflag":1}})
            print(result)
        if choice==7:
            countmodule.countDetails()
        if choice==8:
            b=input("enter the blood group that is required")
            result = collection_name.find({"delflag":0})
            connection=smtplib.SMTP("smtp.gmail.com",587)
            connection.starttls()
            connection.login("practicedigital12@gmail.com","sandhya9@9")
            for i in result:
                message="Dear donar,there is a requirement for " +b+ "bloodgroup in SWIMS hospital please contact us if u are ready to donate the blood"
                connection.sendmail("practicedigital12@gmail.com",i["emailid"],message)
            connection.quit
            print("Mail sent")
            print("Done!") 
        if choice==9:
            break 
except Exception:
    logging.error("Something went wrong")
else:
    print("Your program completed Successfuly")
finally:
    print("Thank you!!") 



        
        
        

