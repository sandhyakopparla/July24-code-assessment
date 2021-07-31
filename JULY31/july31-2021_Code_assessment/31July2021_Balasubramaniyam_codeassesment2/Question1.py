try:
    import requests,json
    data=requests.get("https://jsonplaceholder.typicode.com/todos")
    string=data
    details=string.json()
    completedlist=[i for i in details if i['completed']==True]
    for i in completedlist:
        print(i)
except:
    print("Something went Wrong Please check it")