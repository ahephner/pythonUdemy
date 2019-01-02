import requests

url = "https://icanhazdadjoke.com/"

res = requests.get(url, headers={"Accept": "text/plain"})

#from the api just the joke
print(res.text)

res2 = requests.get(url, headers={"Accept": "application/json"})

#get the JSON
print(res2.text)
#print(type(res2.text)) => <class 'str'>

#this function .json() creates a python dictonary
data = res2.json()
#type dict
print(type(data))
#access one key value pair
print(data["joke"])