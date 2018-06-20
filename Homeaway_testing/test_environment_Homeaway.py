'''
This program demonstrates using environment variables from Python.

If you are using MacOS or if you are using Git Bash on Windows follow the instructions
in this section.  If you are using CMD.EXE with Windows go to the next section.

MacOS/Git Bash instructions:
Go to a Terminal (MacOs) or use Git Bash (Windows).  Then set the variables using
the export command like so:
export TWITTER_CONSUMER_KEY='<your consumer key>'
export TWITTER_CONSUMER_SECRET='<your consumer secret>'
export TWITTER_ACCESS_TOKEN='<your access token>'
export TWITTER_ACCESS_TOKEN_SECRET='<your access token secret>'
Verify they are set:
printenv | sort
After exporting the environment variables run your program:
python test_environment.py

CMD.EXE instructions:
Open a Windows command window.  Then set the environment variables like this:
set TWITTER_CONSUMER_KEY="<your consumer key>"
set TWITTER_CONSUMER_SECRET="<your consumer secret>"
set TWITTER_ACCESS_TOKEN="<your access token>"
set TWITTER_ACCESS_TOKEN_SECRET="<your access token secret>"
Verify that they are set:
set
After exporting the environment variables run your program:
$ python test_environment.py
'''

import os

# Read environment variables for Twitter credential information
consumer_key = os.environ['HOMEAWAY_CONSUMER_KEY']
consumer_secret = os.environ['HOMEAWAY_CONSUMER_SECRET']
google_api_key = os.environ['GOOGLE_MAPS_API_KEY']
# access_token = os.environ['TWITTER_ACCESS_TOKEN']
# access_token_secret = os.environ['TWITTER_ACCESS_TOKEN_SECRET']


