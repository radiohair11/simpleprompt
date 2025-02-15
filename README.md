# Description
This Reddit app scans the subreddit /r/simpleprompts and provides a random writing prompt from the last 100 submissions

# Installation and Usage Instructions
## 1. Sign up or log in to a Reddit account

## 2. Follow the steps [here|https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example#first-steps] to create an app

## 3. Set up a config file
After creating the app, the client secret will be [here|https://www.reddit.com/prefs/apps]

The client_id is the string under "personal use script" in the app description.

Click "edit" to see the client_secret

## 4. Set up the configuration file

Create the file /etc/simplepromptconf.ini and edit it using the example provided in simplepromptconf_example.ini

## 5. Install the requirements
Before installing the requirements, optionally create a virtual env
```python3 -m venv .venv```
```source /path/to/.venv/bin/activate```

Install the requirements
```pip install -rU path/to/simpleprompt/requirements.txt```

## 6. Run the script
```python3 simpleprompt.py```