# Clear Unmoderated

A really quick script to clear all unmoderated posts in all subreddits you mod.

## Requirements

* Python3

Install additional requirements with

```pip install -r requirements.txt```


## Usage

Define a file called `config.py` that declares 4 variables,

```
CLIENT_ID = "client_id"
CLIENT_SECRET = "secret"
USERNAME = "user"
PASSWORD = "pass"
USE_2FA = False
```

Alternatively, you can edit these values within clear_unmod directly.

To run the script:

`python clear_unmod.py`


## Additional notes

To get your client ID and secret, create [an app here](https://www.reddit.com/prefs/apps). Select Script under what type of app you'll be creating


### 2FA

If you are using 2 factor authentication, you must set USE_2FA to True, and input your one time passcode at runtime.