# API Practice from blogpost:
#https://www.dataquest.io/blog/python-api-tutorial/

import requests
import datetime

now = datetime.datetime.now()
day=int(now.day)
month=int(now.month)
year=int(now.year)


# Make a get request to get the latest position of the international space station from the opennotify api.
response = requests.get("http://api.open-notify.org/iss-now.json")
print("A:",response.status_code)
#prints 200 - everything went ok


# making a get request to a non existing endpoint
response = requests.get("http://api.open-notify.org/iss-pass")
print("B:",response.status_code)
#prints 404 - not a valid endpoint

# making another request
response = requests.get("http://api.open-notify.org/iss-pass.json")
print("C:",response.status_code)
#prints 400 - we didn't supply required inputs with the requests


# Set up the parameters we want to pass to the API.
# This is the latitude and longitude of my home in Harrow.
parameters = {"lat": 51.58, "lon": -0.32}

# Make a get request with the parameters.
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
print("D:",response.content)
#this is a byte format


###########################################################################

# json examples

import json
best_food_chains = ["Taco Bell", "Shake Shack", "Chipotle"]
print("E:",type(best_food_chains)) #list

# Use json.dumps to convert best_food_chains to a string.
best_food_chains_string = json.dumps(best_food_chains)
print("F:",type(best_food_chains_string)) #converted to string
print("This is the best food chains string:",best_food_chains_string)
print("G:",type(json.loads(best_food_chains_string))) #back to a list

# Make a dictionary
fast_food_franchise = {
    "Subway": 24722,
    "McDonalds": 14098,
    "Starbucks": 10821,
    "Pizza Hut": 7600
}

# We can also dump a dictionary to a string and load it.
fast_food_franchise_string = json.dumps(fast_food_franchise)
print("H:",type(fast_food_franchise_string))
print("This is the fast food franchise string:",fast_food_franchise_string)


#json from iss api
# Make the same request we did earlier, but .
parameters = {"lat": 51.58, "lon": -0.32}
iss_out = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

# Get the response data as a python object.  Verify that it's a dictionary.
data = iss_out.json()
print("This is the iss_out data type:",type(data))
print("This is the iss_out data:",data)
print("This is the response section of the iss_out data:",data["response"])



#get the risetimes out of the response data
outtxt = "iss_risetimes_%i.%i.%i.txt" % (now.day, now.month, now.year)
outfp = open(outtxt, "w")
outfp.write("ISS risetimes data\n")
iss_response=data["response"]
iss_request=data["request"]

#converting unixtime to normal time
def convtime(t):
    t_n=datetime.datetime.fromtimestamp(int(t)).strftime('%Y-%m-%d %H:%M:%S')
    return t_n

outfp.write("\nToday's datetime is: " + convtime(iss_request['datetime']))
outfp.write("\n\nThe next risetimes of the ISS over Harrow are: ")

for x in iss_response:
    outfp.write("\n"+ str(convtime(x['risetime'])))
outfp.close()


# content type
# Headers is a dictionary
print("These are the headers",response.headers)
# Get the content-type from the dictionary.
print("I:",response.headers["content-type"])


#Astros - how many people in space
# Get the response from the API endpoint.
response = requests.get("http://api.open-notify.org/astros.json")
data = response.json() #dictionary
print("Response:",type(data))
# 3 people are currently in space.
print("J:",data["number"])
print("K:",data)
print("L:",data['people'])
