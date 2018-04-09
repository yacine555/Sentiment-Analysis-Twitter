##READ ME

This is a basic Twitter Sentiment Analyzer in Python 3 using the libraries:
[tweepy](http://www.tweepy.org/) to access the Twitter API
[TextBlob](https://textblob.readthedocs.io/en/dev/) to perform Sentiment Analysis. 
[matplotlib](https://matplotlib.org) to display the result on a Pie chart

Using NLP the script is able able to see how positive or negative each tweet is about whatever topic we choose. 

##Dependencies

* tweepy (http://www.tweepy.org/)
* textblob (https://textblob.readthedocs.io/en/dev/)
* matplotlib (https://matplotlib.org)

Install missing dependencies using [pip](https://pip.pypa.io/en/stable/installing/)

```
$ pip3 install tweepy
$ pip3 install textblob
$ pip3 install matplotlib
$ python3 -m textblob.download_corpora
```



Tweepy requires access to the twitter API and an app must be created at the URL below:
https://apps.twitter.com

Tweepy will need the below information generated from the Twitter API:
- consumer key
- consumer token
- access token
- access token secret

##Usage

Once the dependencies are installed, run the script via the Python 3 console

```
$ python3
>>> # Set the environment variable to access the API token
>>> os.environ['CONSUMER_KEY'] = '<insert your consumer key>'
>>> os.environ['CONSUMER_SECRET'] = '<insert your consumer secret>'
>>> os.environ['ACCESS_TOKEN'] = '<insert your access token>'
>>> os.environ['ACCESS_TOKEN_SECRET'] = '<insert your token secret>'

>>> #Run the script
>>> exec(open("Sentiment_Analysis.py).read())
>>> exit()
```

