import praw

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
prev_link = ""
links = []
for i in range(13, 0, -1):
    title = "The Punisher Discussion Thread - S02E%02d" % i

    body = """This thread is for discussion of The Punisher S02E%02d.

**DO NOT** post spoilers in this thread for any subsequent episodes. Doing so will result in a ban.

[Episode %d Discussion](%s)""" % (i, i + 1, prev_link)

    submission = r.subreddit('Defenders').submit(title=title, selftext=body, send_replies=False)
    submission.mod.approve()
    submission.disable_inbox_replies()
    submission.mod.distinguish('yes')
    submission.mod.lock()
    prev_link = submission.shortlink
    links.append('* [Episode %d Discussion](%s)' % (i, prev_link))

links.reverse()
for link in links:
    print(link + '\n')


# for item in reddit.subreddit('churning').mod.modqueue(limit=None):
# 	Thread(target=approve_post,args=[post]).start()
