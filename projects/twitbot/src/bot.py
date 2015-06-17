#!/usr/bin/env python
import tweepy
#from our keys module (keys.py), import the keys dictionary
from keys import keys
from pprint import pprint
import time
import random
import json

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

api = None
auth = None

strollers = ["@bugaboo", "@maxicosiusa", "@stokkebaby", "@easywalkernl","@urbinibaby", "@kolcraft"]

listener = None
streamer = None

class StreamListener(tweepy.StreamListener):
	def on_status(self, tweet):
		print "Status just came in"

	def on_error(self, status_code):
		print 'Error: ' + repr(status_code)
		return False

	def on_data(self, data):
		global api
		t = json.loads(data)
		try:
			screename = t['user']['screen_name']
			anystroller = random.choice(strollers)
			mytweet = "@{0} maybe {1} could help you with that".format(screename, anystroller)
			print "about to tweet: ", mytweet
			api.update_status(status=mytweet)
		except tweepy.error.TweepError, e:
			print e
			pass


def connect():
	global api, listener, streamer, auth
	print "Connecting to the twitter API"
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
	api = tweepy.API(auth)

def init_responder():
	global api, listener, streamer, auth
	listener = StreamListener()
	streamer = tweepy.Stream(auth=auth, listener=listener)
	streamer.filter(track=['pussy like a stroller'])

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

# def respond_to_pussy():
# 	while True:
# 		time.sleep(2*60)
# 		try:
# 			twts = api.search(q="pussy like a stroller")
# 			if twts:
# 				for t in twts:
# 					screename = t.user.screen_name.encode('utf-8')
# 					anystroller = random.choice(strollers)
# 					mytweet = "@{0} maybe {1} could help you with that".format(screename, anystroller)
# 					print "about to tweet: ", mytweet
# 					api.update_status(status=mytweet)
# 		except tweepy.error.TweepError, e:
# 			print e
# 			pass


def main():
	connect()
	init_responder()
	#respond_to_pussy()
	#tweetforever()
	#search()
	#mentions()

if __name__ == "__main__":
	main()
