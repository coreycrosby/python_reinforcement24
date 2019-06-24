import requests
import json

url = requests.get("https://raw.githubusercontent.com/everypolitician/everypolitician-data/master/countries.json")
countries = url.json()

countries.__class__
# list

for country in countries: 
if country["name"] == "Canada": 
    print(countries.index(country))
# 38

canada = countries[38]
canada['legislatures'][0]['popolo_url']
# https://cdn.rawgit.com/everypolitician/everypolitician-data/f7aa04dafa4e3aee1e03a3386c2653d53b7922ab/data/Canada/Commons/ep-popolo-v1.0.json'

canada_url = requests.get("https://cdn.rawgit.com/everypolitician/everypolitician-data/f7aa04dafa4e3aee1e03a3386c2653d53b7922ab/data/Canada/Commons/ep-popolo-v1.0.json")
canada_gov = canada_url.json()

canada_gov.__class__
#dict

canada_gov.keys()
# dict_keys(['posts', 'persons', 'organizations', 'meta', 'memberships', 'events', 'areas'])

canada_gov['persons'].__class__
# list

name = canada_gov['persons'][143]['name']   
# 'Jean Rioux'