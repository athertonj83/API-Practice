"""With help from the Twitter example from
http://pythoncentral.io/how-to-use-the-twython-twitter-python-library/
"""

from twython import Twython

CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_KEY = ""
ACCESS_SECRET = ""

t=Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

#My timeline
user_timeline = t.get_user_timeline(user_id=186859150,count=2)
print("User tweets")
for tweet in user_timeline:
    print(tweet['text'])


home_timeline=t.get_home_timeline(count=5)
print("\n\nHome timeline")
print(home_timeline)
# for tweet in home_timeline:
#     print(tweet)
    #print("\nTweet:",tweet['text'],"\nUser:",tweet[''])
