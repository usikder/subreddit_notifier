# subreddit_notifier

Originally made to be immediately notified about rare pokemon posts in /r/pokemongoNYC, this script lets you receive texts when new posts show up in a subreddit.

To use:

(1) Generate reddit secrets following these instructions. https://praw.readthedocs.io/en/v3.6.0/pages/oauth.html

(2) Generate twilio secrets by making an account. https://www.twilio.com/

(3) Run `touch log.txt`. 

(4) Deploy an AWS lambda function following these instructions. http://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html