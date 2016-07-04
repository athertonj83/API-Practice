#02 using twitter
import requests
import oauth2 as oauth
import json

# import os.path, sys
# # Add current dir to search path.
# sys.path.insert(1,'C:\Users\Jen\Documents\Python for Windows')
# # Add module from the current directory.
# sys.path.insert(1, os.path.dirname(os.path.abspath(os.path.realpath(__file__))) + "/dir")
#
# import twitter_auth



CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_KEY = "-"
ACCESS_SECRET = ""

consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
client = oauth.Client(consumer, access_token)

client.verify_credentials()

timeline_endpoint = "https://api.twitter.com/1.1/statuses/home_timeline.json?count=1"
#response,data = client.request(timeline_endpoint)
this=client.request(timeline_endpoint)


# print("This is response:",response)
# print(type(response)) #response type
# print("This is data:",data)
# print(type(data)) #byte type
print("This is this:",this)
print(type(this)) # tuple type

data5=response,data.json()
print(data5)




# Get the response data as a python object.  Verify that it's a dictionary.
#data1 = data.json()
#print(type(data1)) #dictionary



#print(data['user'])



# print(type(data))
#print(data[0])
#print(data[1])

# data1=json.loads(data)
# print(data1)


#print(type(response))
#data1=data.json()
#
#
# print(data1)

#tweets = json.loads(data)
# for tweet in data:
#     print(tweet['text'])
