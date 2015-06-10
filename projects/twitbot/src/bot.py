#!/usr/bin/env python
import tweepy
#from our keys module (keys.py), import the keys dictionary
from keys import keys
from pprint import pprint
import time
import random

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

api = None


strollers = ["@bugaboo", "@maxicosiusa", "@stokkebaby", "@easywalkernl","@urbinibaby", "@kolcraft"]

def connect():
	global api
	print "Connecting to the twitter API"
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
	api = tweepy.API(auth)

def search():
	global api
	twts = api.search(q="Hello World!")
	#pprint(twts[0])
	print "*"*80
	print twts[0].text
	# for t in twts:
	# 	pprint( t )

def mentions():
	mentions = api.mentions_timeline(count=1)
	if mentions:
		for m in mentions:
			print(m)
	else:
		print "No mentions yet"

def tweetforever():
	filename=open('lines.txt','r')
	f=filename.readlines()
	filename.close()

	for line in f:
	     api.update_status(status=line)
	     print line
	     time.sleep(60) # Sleep for 1 hour

def respond_to_pussy():
	while True:
		try:
			twts = api.search(q="pussy like a stroller")
			if twts:
				for t in twts:
					screename = t.user.screen_name.encode('utf-8')
					anystroller = random.choice(strollers)
					mytweet = "@{0} maybe {1} could help you with that".format(screename, anystroller)
					print "about to tweet: ", mytweet
					api.update_status(status=mytweet)
		except tweepy.error.TweepError, e:
			pass


def main():
	connect()
	respond_to_pussy()
	#tweetforever()
	#search()
	#mentions()

if __name__ == "__main__":
	main()
