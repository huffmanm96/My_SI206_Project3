# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.
import tweepy
import tokens

print ("Name: Madison Huffman")
print ("UM ID: 34109303")
print("\n")

# Boilerplate code here
auth = tweepy.OAuthHandler(tokens.consumer_key,tokens.consumer_secret)
auth.set_access_token(tokens.access_token,tokens.access_token_secret)

api = tweepy.API(auth)
#Now we can Create Tweet
try:
    api.update_with_media('umsi_internal_yellow_M2.jpg',"#UMSI-206 #Proj3")
    print ("Success!")
except:
    print ("Fail... womp.")


