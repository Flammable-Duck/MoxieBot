import requests

def get_fortune():
    "gets a fortune from https://github.com/ef-gy/fortuned, some random api for the UNIX fortune command"
    response = requests.get("https://fortuneapi.herokuapp.com/")
    unicode_quote =  bytes(response.text, "utf-8").decode("unicode_escape")
    return "```" + unicode_quote.strip(" \" ")[:-3] + "```"

