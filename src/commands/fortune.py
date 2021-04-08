import requests
import json

def get_fortune():
    "gets a fortune from https://github.com/ef-gy/fortuned, some random api for the UNIX fortune command"
    response = requests.get("https://fortuneapi.herokuapp.com/")
    return response.text

