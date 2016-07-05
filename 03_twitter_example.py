""" example runthrough from
http://social-metrics.org/twitter-user-data/
"""

import sys
import string
import json
from twython import Twython
import datetime

now = datetime.datetime.now()
day=int(now.day)
month=int(now.month)
year=int(now.year)


#Bringing in my personal twitter keys
with open("C:/Users/Jen/Documents/Python for Windows/twitter_auth.py") as f:
    code = compile(f.read(), "C:/Users/Jen/Documents/Python for Windows/twitter_auth.py" , 'exec')
    exec(code)

CONSUMER_KEY = auth.ckey
CONSUMER_SECRET = auth.csecret
ACCESS_KEY = auth.accessk
ACCESS_SECRET = auth.accesss

t = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

screen_names = "jennifera83"
users = t.lookup_user(screen_name = screen_names)

outfn = "twitter_user_data_%i.%i.%i.txt" % (now.day, now.month, now.year)

fields = "id screen_name name created_at url followers_count friends_count statuses_count \
    favourites_count listed_count \
    contributors_enabled description protected location lang expanded_url".split()

print("This is string:",string)
outfp = open(outfn, "w")
#outfp.write("\t".join(string) + "\n")  # header
outfp.write("Twitter data for " + screen_names + "\n")

#THE VARIABLE 'USERS' CONTAINS INFORMATION OF THE 32 TWITTER USER IDS LISTED ABOVE
#THIS BLOCK WILL LOOP OVER EACH OF THESE IDS, CREATE VARIABLES, AND OUTPUT TO FILE
for entry in users:
    #CREATE EMPTY DICTIONARY
    r = {}
    for f in fields:
        r[f] = ""
    #ASSIGN VALUE OF 'ID' FIELD IN JSON TO 'ID' FIELD IN OUR DICTIONARY
    r['id'] = entry['id']
    #SAME WITH 'SCREEN_NAME' HERE, AND FOR REST OF THE VARIABLES
    r['screen_name'] = entry['screen_name']
    r['name'] = entry['name']
    r['created_at'] = entry['created_at']
    r['url'] = entry['url']
    r['followers_count'] = entry['followers_count']
    r['friends_count'] = entry['friends_count']
    r['statuses_count'] = entry['statuses_count']
    r['favourites_count'] = entry['favourites_count']
    r['listed_count'] = entry['listed_count']
    r['contributors_enabled'] = entry['contributors_enabled']
    r['description'] = entry['description']
    r['protected'] = entry['protected']
    r['location'] = entry['location']
    r['lang'] = entry['lang']
    #NOT EVERY ID WILL HAVE A 'URL' KEY, SO CHECK FOR ITS EXISTENCE WITH IF CLAUSE
    if 'url' in entry['entities']:
        r['expanded_url'] = entry['entities']['url']['urls'][0]['expanded_url']
    else:
        r['expanded_url'] = ''
    # #CREATE EMPTY LIST
    # lst = []
    # #ADD DATA FOR EACH VARIABLE
    # for f in fields:
    #     lst.append(r[f])
    # print("This is lst:",lst)

    #INTO A STRING (JA)
    str1=""
    for f in fields:
        str1=str1+str(f)+" : "+str(r[f])+"\n"
    print("This is str1:",str1)
    #WRITE ROW WITH DATA IN LIST
    outfp.write("\n"+ str1)

outfp.close()
