import tweepy
import time

consumer_key = 'AnoT59dptdzC5EfmP7pKNEOig'
consumer_secret = 'KdJUnRGWPxzrOuirwNruOFgQlXwbCIOJzodlOnbiKsmhJcEWsS'
key = '447938059-Z2owpm4FQOXBGGoKXQfC8kCUt4akBk8vde5TOZvZ'
secret = 'sbp4FCt0okPyeZR64PvTJTLFXcmvWhBPjucBOBZWxFF1e'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

hashtag = "100daysofcode"
tweetNumber = 10

tweets = tweepy.Cursor(api.search, hashtag).items(tweetNumber)

def searchbot():
    for tweet in tweets:
        try:
            tweet.retweet()
            print("Retweet Done!")
            time.sleep(2)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(2)

searchbot()
