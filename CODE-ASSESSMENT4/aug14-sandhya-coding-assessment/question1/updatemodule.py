import pymongo
client=pymongo.MongoClient("mongodb://localhost:27017/")
mydatabase=client['DonarsDb']
collection_name=mydatabase['donars']
def updatedetails():
    while(True):
        print("1.update the name")
        print("2.update the address")
        print("3.update the bloodgroup ")
        print("4.update the pincode")
        print("5.update last_donated date")
        print("6.update place")
        print("7.exit")
        ch=int(input("enter your choice"))
        if ch==1:
            m=input("enter the mobile_number")
            n=input("enter the name")
            result=collection_name.update_one({"mobile_number":m},{"$set":{"name":n}})
            print(result)
        if ch==2:
            m=input("enter the mobile_number")
            a=input("enter the address")
            result=collection_name.update_one({"mobile_number":m},{"$set":{"address":a}})
            print(result)
        if ch==3:
            m=input("enter the mobile_number")
            b=input("enter the blood group")
            result=collection_name.update_one({"mobile_number":m},{"$set":{"bloodgroup":b}})
            print(result)
        if ch==4:
            m=input("enter the mobile_number")
            p=input("enter the pincode")
            result=collection_name.update_one({"mobile_number":m},{"$set":{"pincode":p}})
            print(result)
        if ch==5:
            m=input("enter the mobile_number")
            l=input("enter the last_donated_date")
            result=collection_name.update_one({"mobile_number":m},{"$set":{"last_denoted_date":l}})
            print(result)
        if ch==6:
            m=input("enter the mobile_number")
            l=input("enter the place")
            result=collection_name.update_one({"mobile_number":m},{"$set":{"place":l}})
            print(result)
        if ch==7:
            break
