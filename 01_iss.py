# API Practice from blogpost:
#https://www.dataquest.io/blog/python-api-tutorial/

import requests


# Make a get request to get the latest position of the international space station from the opennotify api.
response = requests.get("http://api.open-notify.org/iss-now.json")
print(response.status_code)
#prints 200 - everything went ok


# making a get request to a non existing endpoint
response = requests.get("http://api.open-notify.org/iss-pass")
print(response.status_code)
#prints 404 - not a valid endpoint

# making another request
response = requests.get("http://api.open-notify.org/iss-pass.json")
print(response.status_code)
#prints 400 - we didn't supply required inputs with the requests


# Set up the parameters we want to pass to the API.
# This is the latitude and longitude of my home in Harrow.
parameters = {"lat": 51.58, "lon": -0.32}

# Make a get request with the parameters.
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
print(response.content)
#this is a byte format


###########################################################################

# json examples

import json
best_food_chains = ["Taco Bell", "Shake Shack", "Chipotle"]
print(type(best_food_chains)) #list

# Use json.dumps to convert best_food_chains to a string.
best_food_chains_string = json.dumps(best_food_chains)
print(type(best_food_chains_string)) #converted to string
print(type(json.loads(best_food_chains_string))) #back to a list

# Make a dictionary
fast_food_franchise = {
    "Subway": 24722,
    "McDonalds": 14098,
    "Starbucks": 10821,
    "Pizza Hut": 7600
}

# We can also dump a dictionary to a string and load it.
fast_food_franchise_string = json.dumps(fast_food_franchise)
print(type(fast_food_franchise_string))


#json from iss api
# Make the same request we did earlier, but .
parameters = {"lat": 51.58, "lon": -0.32}
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

# Get the response data as a python object.  Verify that it's a dictionary.
data = response.json()
print(type(data))
print(data)


# content type
# Headers is a dictionary
print(response.headers)
# Get the content-type from the dictionary.
print(response.headers["content-type"])


#Astros - how many people in space
# Get the response from the API endpoint.
response = requests.get("http://api.open-notify.org/astros.json")
data = response.json()

# 9 people are currently in space.
print(data["number"])
print(data)
