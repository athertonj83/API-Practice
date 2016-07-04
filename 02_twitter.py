#02 using twitter - not got this working yet
import requests
import oauth2 as oauth
import json

#Bringing in my personal twitter keys
with open("C:/Users/Jen/Documents/Python for Windows/twitter_auth.py") as f:
    code = compile(f.read(), "C:/Users/Jen/Documents/Python for Windows/twitter_auth.py" , 'exec')
    exec(code)

CONSUMER_KEY = auth.ckey
CONSUMER_SECRET = auth.csecret
ACCESS_KEY = auth.accessk
ACCESS_SECRET = auth.accesss

consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
client = oauth.Client(consumer, access_token)



timeline_endpoint = "https://api.twitter.com/1.1/statuses/home_timeline.json?count=1"
#response,data = client.request(timeline_endpoint)
this=client.request(timeline_endpoint)


# print("This is response:",response)
# print(type(response)) #response type
# print("This is data:",data)
# print(type(data)) #byte type
print("This is this:",this)
print(type(this)) # tuple type
#print(this['screen_name'])

# data5=response,data.json()
# print(data5)




# Get the response data as a python object.  Verify that it's a dictionary.
data1 = this.json()
print(type(data1)) #dictionary



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
