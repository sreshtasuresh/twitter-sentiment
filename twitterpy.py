import tweepy
from textblob import TextBlob
consumer_key = 'IT2lCcf93iyF1mkxdng0LLTcw'
consumer_secret = 'VoZnYrrAyX9hh9wRLGtkXNeRHGizFSgIxJ8j1CLVt1UTw8t5z2'
access_token = '127166493-On5VJhMjCspjqSh5iZwNVY7D4wDxVvFQrYNNEGVL'
access_token_secret = 'u7p27jWuxKlRmqjcnpVMjBIEENRdi9mEKoqJfzGQZxBzZ'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api=tweepy.API(auth)
public_tweets= api.search('salah')
for tweet in public_tweets:
	print(tweet.text)
	analysis=TextBlob(tweet.text)
	print(analysis.sentiment)