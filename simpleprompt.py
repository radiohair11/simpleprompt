# simpleprompt.py
# simpleprompt.py chooses a random title from /r/simpleprompts
# author: dave jenkins, https://github.com/radiohair11

import praw
import logging
import random
import configparser
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

logger = logging.getLogger(__name__)

logging.basicConfig(filename='simpleprompt.log', level=logging.INFO)

config = configparser.ConfigParser()
config.read('/etc/simplepromptconf.ini')

logger.info(config['SECRETS']['client_id'])
logger.info(config['SECRETS']['client_secret'])
logger.info(config['SECRETS']['user_agent'])

reddit = praw.Reddit(
    client_id=config['SECRETS']['client_id'],
    client_secret=config['SECRETS']['client_secret'],
    user_agent=config['SECRETS']['user_agent'],
)

subreddit = reddit.subreddit("simpleprompts")
logger.info(f"Connected to subreddit {subreddit} as read only {reddit.read_only}")
submission_titles = []

submissions = subreddit.new(limit=100)

for submission in submissions:
    submission_titles.append(submission.title)
random_submission = random.choice(submission_titles)

logger.info("\n")
logger.info(random_submission)

clear_console()
print(random_submission)
print("press enter when done")
input()
clear_console()