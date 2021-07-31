import re
import smtplib
try:
    print("*****MENU*****")
    print("1. Tea (Rs.7)")
    print("2. Coffee (Rs.10)")
    print("3. Masala Dosa (Rs.50)")
    a = int(input('Enter the number of cup of TEA (0 if you don\'t want)  -  '))
    b = int(input('Enter the number of cup of COFFEE (0 if you don\'t want)  -  '))
    c = int(input('Enter the number of MASALA DOSA (0 if you don\'t want)  -  '))
    d = int(input('you have completed the order now press 4 to get your bill - '))
    email = input('Enter your email id - ')
    emailid=re.match('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$',email)
    if emailid:
        Email=email
    connection=smtplib.SMTP("smtp.gmail.com",587)
    connection.starttls()
    connection.login("gulshan062132@gmail.com","Gullu@2132")
    if(d==4):
        total =a*7+b*10+c*50
    message='your total Amount is '+ str(total)
    connection.sendmail("gulshan062132@gmail.com",Email, message)
    connection.quit()
except Exception:
    print("You enter wrong input")

else:
    print("your order placed Successfully")
    print('Your total Amount is - ',total)
finally:
    print("Thank you!!")
