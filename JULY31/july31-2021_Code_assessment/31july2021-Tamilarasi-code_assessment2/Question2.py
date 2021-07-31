import smtplib
#food Item in list
Food_menu=["Tea","Coffee","Masala_Dosa"]

#Using dictionary
Total=dict.fromkeys(Food_menu,0)
while(True):
    print("Hi! Enter Your Delicious Food: ")
    print("1.Tea(Rs.7)")
    print("2.Coffee(Rs.10)")
    print("3.Masala_Dosa(Rs.50)")
    print("4.View Bill and Email")

    #menu Choice
    Choice=int(input())
    if Choice == 1:
        Tea=int(input("Enter Your Count Of Tea Order:"))
        Total["Tea"] = Total["Tea"] + Tea
    elif Choice == 2:
        Coffee=int(input("Enter Your Count Of Coffee Order:"))
        Total["Coffee"] = Total["Coffee"] + Coffee
    elif Choice == 3:
        Masala_Dosa=int(input("Enter Your Count Of Masala Dosa Order:"))
        Total["Masala_Dosa"] = Total["Masala_Dosa"] + Masala_Dosa
    elif Choice == 4:
        break
    else:
        print("Enter The Correct option: ")
print(Total)

#Count the Price
Data="Food_Item-> Count- Price\n"
print(Total["Tea"])
if Total["Tea"] > 0:
    Data=Data+"Tea-> "+str(Total["Tea"])+"- "+str(7*Total["Tea"])+"Rupees,  "

if Total["Coffee"] > 0:
    Data=Data+"Coffee-> "+str(Total["Coffee"])+"- "+str(10*Total["Coffee"])+"Rupees,  "
    
if Total["Masala_Dosa"] > 0:
    Data=Data+"Masala_Dosa-> "+str(Total["Masala_Dosa"])+"- "+str(50*Total["Masala_Dosa"])+"Rupees.  "
print(Data)

#send mail
connection=smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login("tamilarasiiprimed@gmail.com","Iprimed@123")
connection.sendmail("tamilarasiiprimed@gmail.com","tamilarasiifet@gmail.com",Data)
connection.quit
print("Total Bill")
print("Mail Send Successfully! Happy Customer:)")