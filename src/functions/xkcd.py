
import requests
import json
from random import randint

def latest_xkcd():
    "returns latest xkcd"
    url = "https://xkcd.com/info.0.json"
    response = requests.request("GET", url)
    data = json.loads(response.text)
    return data

def random_xkcd():
    "returns random xkcd"
    url = "http://xkcd.com/" + str(randint(1, latest_xkcd()["num"])) + "/info.0.json"
    response = requests.request("GET", url)
    data = json.loads(response.text)
    return data


#print(json.dumps(random_xkcd(), indent=4, sort_keys=True)) #pretty JSON, for debugging
