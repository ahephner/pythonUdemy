import requests

res = requests.get("https://news.ycombinator.com/")

print(res)

print(res.ok)
#get html
res.text

#get headers
res.headers