import requests
import json

def search_urban(word):
    "returns the top definiton of a word at urban dictionary"
    url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"
    querystring = {"term": word}
    headers = {
        'x-rapidapi-key': "46759b7bd6msh35d5ee9a8cdba2cp12bbb9jsn95f35305f9a3",
        'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = json.loads(response.text)
    ###return json.dumps(data, indent=4, sort_keys=True) #pretty JSON, for debugging
    #definition = data['list'][0]['definition'].replace("\n", "")
    #finalstring = "from the Urban Dictionary:\n\n" + "**" +  word + "**" + "\n" + definition + "\n\n" + "*" + data['list'][0]['example'] + "*"
    return data


#print(search_urban("test"))