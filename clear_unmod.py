import praw
from threading import Thread
import time
try:
	# try to read from config.py
	from account import *
except:
	CLIENT_ID = "client_id"
	CLIENT_SECRET = "secret"
	USERNAME = "user"
	PASSWORD = "pass"
	USE_2FA = False

if USE_2FA:
	token = input("Input 2FA Token here: ")
	PASSWORD = PASSWORD + ":" + token

# Generate reddit instance from details in account
r = praw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, user_agent="approve_unmod", username=USERNAME,
                password=PASSWORD)

def approve_post(post):
	post.mod.approve()
	print(post.permalink)

# Iterate over all subreddits the user mods
	# Get all unmoderated posts
# Approve them and print ids
def clear():
	for post in r.subreddit('churning').mod.modqueue(limit=None):
		Thread(target=approve_post,args=[post]).start()
		time.sleep(0.25)
	clear()

clear()

# for item in reddit.subreddit('churning').mod.modqueue(limit=None):
# 	Thread(target=approve_post,args=[post]).start()		