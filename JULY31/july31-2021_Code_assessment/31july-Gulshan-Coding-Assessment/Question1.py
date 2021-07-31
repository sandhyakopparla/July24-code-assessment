
import json
import requests
data=requests.get("https://jsonplaceholder.typicode.com/todos")
try:
    def api(data):
        li=data.json()     
        new_li=[x for x in li if x["completed"]==True]
        return new_li    
    print(api(data))
except IndexError:
    print('Your List Index is out of Range')
else:
    print('Your program completed successfully')
finally:
    print("Thank You!!")