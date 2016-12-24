#!/usr/local/env python

import praw
from twilio.rest import TwilioRestClient

# See praw documenation for how to generate these
REDDIT_CLIENT_ID = 'reddit_client_id'
REDDIT_CLIENT_SECRET = 'reddit_client_secret'
REDDIT_USER_AGENT = 'reddit_user_agent'

# See twilio documentation for how to generate these
TWILIO_SID = 'twilio_sid'
TWILIO_SECRET = 'twilio_secret'
TWILIO_NUMBER = 'twilio_number'

MY_NUMBER = 'my_number'
SUBREDDIT = 'subreddit'

# See AWS documentation for how to run this script as a lambda

def job(event, context):
	reddit = praw.Reddit(
		client_id=REDDIT_CLIENT_ID, 
		client_secret=REDDIT_CLIENT_SECRET, 
		user_agent=REDDIT_USER_AGENT,
	)

	twilio = TwilioRestClient(TWILIO_SID, TWILIO_SECRET)

	pokemons = ['lickitung', 'dragonite', 'chansey', 'hitmonchan']

	processed_submissions = [l.rstrip('\n') for l in open('log.txt', 'r')]
	appender = open('log.txt', 'a')

	for submission in reddit.subreddit(SUBREDDIT).new(limit=10):
		if submission.fullname in processed_submissions:
			continue
		for pokemon in pokemons:
			if pokemon in submission.title.lower():
				appender.write(submission.fullname + '\n')
				twilio.messages.create(
					to=MY_NUMBER, 
					from_=TWILIO_NUMBER, 
					body=submission.title,
				)