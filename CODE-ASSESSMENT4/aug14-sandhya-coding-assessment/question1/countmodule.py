import pymongo
client=pymongo.MongoClient("mongodb://localhost:27017/")
mydatabase=client['DonarsDb']
collection_name=mydatabase['donars']
def countDetails():
    while(True):
        print("1.count the bloodgroup")
        print("2.exit")
        ch=int(input("enter the choice"))
        if ch==1:
            bg=input("enter the blood group:")
            result=collection_name.count_documents({"bloodgroup":bg,"delflag":0})
            print("count=",result)
        if ch==2:
            break