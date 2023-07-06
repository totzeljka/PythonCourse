import requests
import config

# kreirati novi projekat pyyelp i
# novi fajl u njemu app.py,
# https://docs.developer.yelp.com/docs/endpoints-4, https://www.yelp.com/developers/v3/manage_app
# u terminalu : pipenv install requests

url = "https://api.yelp.com/v3/businesses/search"
headers = {
    "Autorisation": "Bearer" + config.api_key
}

params = {
    "location": "Novi Sad"
}

responce = requests.get(url, headers=headers, params=params)
bussineses = responce.json()["businesses"]
names = [bussines["name"]
         for bussines in bussineses if bussines["rating"] > 4.5]
print(names)
