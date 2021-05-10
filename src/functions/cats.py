import json

import requests


def get_cat_pic():
    response = requests.get("https://api.thecatapi.com/v1/images/search")
    return json.loads(response.url())
    #return response.json()

print(get_cat_pic())
