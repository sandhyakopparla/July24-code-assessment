try:
    menu=["Tea","Coffee","MasalaDosa"]
    menudict=dict.fromkeys(menu,0)

    while(True):
        print("Enter Your option: ")
        print("1)  Tea(Rs.7)")
        print("2)  Coffee(Rs.10)")
        print("3)  Masala Dosa(Rs.50)")
        print("4)  View Bill and Email")
        option=int(input())
        if option==1:
            teacount=int(input("Enter the how many teas want :"))
            menudict['Tea']=menudict['Tea']+teacount
        elif option==2:
            coffeecount=int(input("Enter the how many Coffee want :"))
            menudict['Coffee']=menudict['Coffee']+coffeecount
        elif option==3:
            Masalacount=int(input("Enter the how many Masaladosa want :"))
            menudict['MasalaDosa']=menudict['MasalaDosa']+Masalacount
        elif option==4:
            break
        else:
            print("Enter The Correct option: ")
    print(menudict)
    message="Dish       Quantity       Price\n"
    #print("Dish       Quantity       Price")
    print(menudict["Tea"])
    if menudict['Tea']>0:
        message=message+'Tea          '+str(menudict['Tea'])+'             '+str(7*menudict['Tea'])+'Rs\n'
    if menudict['Coffee']>0:
        message=message+'Coffee       '+str(menudict['Coffee'])+'             '+str(10*menudict['Coffee'])+'Rs\n'
    if menudict['MasalaDosa']>0:
        message=message+'MasalaDosa   '+str(menudict['MasalaDosa'])+'             '+str(50*menudict['MasalaDosa'])+'Rs\n'
    message = message+'Total price                '+str(7*menudict['Tea']+10*menudict['Coffee']+50*menudict['MasalaDosa'])+'Rs\n'
    print(message)
    import smtplib
    connection=smtplib.SMTP("smtp.gmail.com",587)
    connection.starttls()
    connection.login("balu08062000@gmail.com","balu@123")
    connection.sendmail("balu08062000@gmail.com","balusaravanan862@gmail.com",message)
    connection.quit
    print("Mail sent")
except:
    print("SomeThing went Wrong please check it")