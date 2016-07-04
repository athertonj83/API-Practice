"""With help from the Twitter example from
http://pythoncentral.io/how-to-use-the-twython-twitter-python-library/
"""
from twython import Twython

#Bringing in my personal twitter keys
with open("C:/Users/Jen/Documents/Python for Windows/twitter_auth.py") as f:
    code = compile(f.read(), "C:/Users/Jen/Documents/Python for Windows/twitter_auth.py" , 'exec')
    exec(code)

CONSUMER_KEY = auth.ckey
CONSUMER_SECRET = auth.csecret
ACCESS_KEY = auth.accessk
ACCESS_SECRET = auth.accesss


t=Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

#My timeline
user_timeline = t.get_user_timeline(user_id=186859150,count=2)
print("User tweets")
for tweet in user_timeline:
    print(tweet['text'])


home_timeline=t.get_home_timeline(count=5)
print("\n\nHome timeline")
for tweet in home_timeline:
    print(tweet['text'])
