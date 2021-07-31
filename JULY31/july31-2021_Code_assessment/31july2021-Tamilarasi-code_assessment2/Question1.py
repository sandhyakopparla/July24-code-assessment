import requests,json
data=requests.get("https://jsonplaceholder.typicode.com/todos")
ExtractedData=data.json() 
print([i for i in ExtractedData if i["completed"]==True ])