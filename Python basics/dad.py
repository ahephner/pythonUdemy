import requests
from random import choice
query = input('what do you want to search for?')
url = "https://icanhazdadjoke.com/search"
res = requests.get(url,
                    headers={"Accept": "application/json"},
                    params={"term": query}
                    ).json()


jokes = res['total_jokes']
results = res["results"]
if jokes > 1:
    print('alot of jokes ' +str(jokes))
    print(choice(results)["joke"])
elif jokes == 1:
    print("I know one joke:")
    print(results[0]['joke'])
else:
    print(f'no jokes for {query}')