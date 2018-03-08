import praw

try:
	#try to read from config.py
	from account import *
except:
	CLIENT_ID = "client_id"
	CLIENT_SECRET = "secret"
	USERNAME = "user"
	PASSWORD = "pass"


# Generate reddit instance from details in account
r = praw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, user_agent="approve_unmod", username=USERNAME,
	password=PASSWORD)


# Iterate over all subreddits the user mods
for sub in r.user.moderator_subreddits(limit=None):
	# Get all unmoderated posts
	posts = [post for post in sub.mod.unmoderated(limit=None)]
	# Approve them and print ids
	for post in posts:
		post.mod.approve()
		print(post)
