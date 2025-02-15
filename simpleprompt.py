# simpleprompt.py
# simpleprompt.py chooses a random title from /r/simpleprompts
# author: dave jenkins, https://github.com/radiohair11

import praw
import logging
import random
import tkinter as tk
import configparser

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    
    window.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

window_width = 800
window_height = 50

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

window = tk.Tk()
window.title("Simple Prompt")

text_label = tk.Label(window, text=random_submission, padx=20, pady=10)
text_label.pack()

# Start the Tkinter event loop
center_window(window, window_width, window_height)
window.mainloop()
