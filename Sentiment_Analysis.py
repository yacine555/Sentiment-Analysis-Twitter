#Sentiment Analysis usng Twitter API and TextBlob for sentiment Analysis
#
#https://apps.twitter.com
#Owner	ybouakkaz

import os
import tweepy
from textblob import TextBlob
import numpy as np
import matplotlib.pyplot as plt

class SearchPolarities:
  positive = 0.0
  neutral = 0.0
  negative = 0.0


consumer_key = os.environ['CONSUMER_KEY']
consumer_secret = os.environ['CONSUMER_SECRET']

access_token = os.environ['ACCESS_TOKEN']
access_token_secret = os.environ['ACCESS_TOKEN_SECRET']

try:
	auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
	auth.set_access_token(access_token,access_token_secret)
	api = tweepy.API(auth)
except:
    print("Error: Authentication Failed")

#Set Application parameters
analysisQuery = input("Enter keyword you want to apply the sentiment analysis: ")
print('Term to analyze is: ' + analysisQuery )
tweetLang = 'English'

#Search the tweet to analyze based on input 
#http://docs.tweepy.org/en/v3.6.0/api.html#API.search
tweets = api.search(analysisQuery)
#tweets = api.search(analysisQuery,lang=tweetLang)

if not tweets:
	exit()


search_polarities = SearchPolarities()


#Perform Sentiment Analysis on Tweets
for tweet in tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	#search_polarities.append(analysis.sentiment.polarity)

	print(analysis.sentiment.polarity)

	if (analysis.sentiment.polarity > 0.00):
		search_polarities.positive +=1
	elif (analysis.sentiment.polarity < 0.00):
		search_polarities.negative +=1
	else:
		search_polarities.neutral +=1


search_polarities.positive = search_polarities.positive/len(tweets)*100
search_polarities.negative = search_polarities.negative/len(tweets)*100
search_polarities.neutral = search_polarities.neutral/len(tweets)*100

print('\n Result of sentiment analysis for term ' + analysisQuery + ':\n')
print('%s : %0.3f' % ('Positive', search_polarities.positive))

#use matplotlib to display values on graph
labels = ['Positive ['+ str(search_polarities.positive)+'%]','Negative ['+ str(search_polarities.negative)+'%]','Neutral  ['+ str(search_polarities.neutral)+'%]']
sizes = [search_polarities.positive,search_polarities.negative,search_polarities.neutral]
colors = ['green','red','gray']

patches = plt.pie(sizes, colors=colors)
plt.legend(patches[0], labels,loc="best")
plt.title('Twitter sentiment analysis of term ' + analysisQuery)
plt.tight_layout()
plt.show()




