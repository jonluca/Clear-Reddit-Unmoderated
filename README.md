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
```

Alternatively, you can edit these values within clear_unmod directly.

To run the script:

`python clear_unmod.py`