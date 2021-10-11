import tweepy
import os
import requests
import json
from google.cloud import language


consumer_key = 'SAk1EcgwgIzYbMYK6UdgxoOjq'
consumer_secret = '5WrznTMrKTXu2DX95EIGCGuIzrIrdbeiJ77pOvH5SkrCjkNoS5'
access_token = '1441509311604133896-Hh0fS3sOBiNLqpwRrTG6TZMFUuJ4xB'
access_token_secret = 'aHvrrLjY8THLkh7JNaljhHcBaQhA8wKkVFEYm9HCw2Gj2'

auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)
results = api.search_tweets(q=input_str, count=500, lang = "en")
user_id = "ruiling" 
async def musiccontrols(api, create_friendship):
    api.create_friendship(user_id)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print (tweet.user.name,"said: ",tweet.text, "\n")


keywords = 'Biden' 
number = 5 

tweets=[ ]
likes=[]

for tweet in tweepy.Cursor(api.search_tweets, q=keywords, lang="en").items(number):
    tweets.append(tweet._json)#search the specific content
    likes.append(tweet.favorite_count)        

table = pd.json_normalize(tweets) 
a=table['created_at'] 
b=table['text']   
    

df=pd.DataFrame({"time":a,"likes":likes,"tweets":b})

pd.set_option('display.width',5000)
print(df)

content = tweepy.Cursor(api.search_tweets, q=keywords, lang="en").items(number)

n = []
s = []
for tweet in content:
    n.append(tweet.text)
    analysis = TextBlob(tweet.text)
    s.append(analysis.sentiment.polarity)

for sen in range(0,len(s)):
    print(f"the sentiment score of sentence {sen} is {s[sen]}")

def analysis(score):
  if score < 0:
    return 'Negative'
  elif score==0:
    return 'Middle'
  else:
    return 'Positive'

for i in s:
	a = analysis(i)
	print(f"the analysis of the semtence {sen} is {a}")

def main():
    print(search_tweets(keyword,total_tweets))
    print("Sentiment score is: ", end= " ")
    print(sentiment.score)
    print("Sentiment magnitude is: ", end=" ")
    print(sentiment.magnitude)
    print("Sentiment status is: ", end=" ")
    print(content_status())

if __name__ == "__main__":
    main()