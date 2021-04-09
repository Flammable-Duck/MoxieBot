import requests
import json

def get_cat_pic():
    response = requests.get("https://api.thecatapi.com/v1/images/search")
    data = json.loads(response.url())

    return data
    #return response.json()

print(get_cat_pic())
