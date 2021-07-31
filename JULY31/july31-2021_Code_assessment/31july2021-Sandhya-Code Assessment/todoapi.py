import json
import requests
data=requests.get("https://jsonplaceholder.typicode.com/todos")
ExtractedData=data.json()
li=[x for x in ExtractedData if x["completed"]==True]
print(li)