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
	PASSWORD = PASSWORD + ":" + str(token)

# Generate reddit instance from details in account
r = praw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, user_agent="approve_unmod", username=USERNAME,
                password=PASSWORD)
for i in range(1,14):
	title = "Daredevil Discussion Thread - S03E%02d" % i

	body = """This thread is for discussion of Daredevil S02E%02d."

**DO NOT** post spoilers in this thread for any subsequent episodes. Doing so will result in a ban.

[Episode %d Discussion]()""" % (i, i+1)

	submission = r.subreddit('Defenders').submit(title = title, selftext=body, send_replies=False)

# for item in reddit.subreddit('churning').mod.modqueue(limit=None):
# 	Thread(target=approve_post,args=[post]).start()		