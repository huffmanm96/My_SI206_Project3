# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.

import tweepy
from textblob import TextBlob
import tokens


# Boilerplate code here
auth = tweepy.OAuthHandler(tokens.consumer_key,tokens.consumer_secret)
auth.set_access_token(tokens.access_token,tokens.access_token_secret)

api = tweepy.API(auth)
#Now we can Create Tweets, Delete Tweets, and Find Twitter Users

polarity = 0
subjectivity = 0
count = 0
print ('\n')
print ("~~~~~~~~ TWEETS ~~~~~~~~")
print ('\n')
public_tweets = api.search('ElectionNight')
for tweet in public_tweets:
     print(tweet.text)
     count += 1
     analysis = TextBlob(tweet.text)
     print (analysis.sentiment)
     polarity += analysis.sentiment.polarity
     subjectivity += analysis.sentiment.subjectivity
     print ('\n')
     
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Average subjectivity is " + str(subjectivity/count))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Average polarity is " + str(polarity/count))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print ('\n')
