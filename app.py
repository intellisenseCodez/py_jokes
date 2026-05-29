import requests
import json

res = requests.get(url="https://v2.jokeapi.dev/joke/Any?type=single")

joke = res.json()["joke"]

print(joke)