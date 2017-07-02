## Example of reading a large JSON file using pymongo

# Imports
import json
from urllib.request import urlopen
import pymongo

# Connect to Mongo
connection = pymongo.MongoClient("mongodb://localhost")

# Connect to Database
db = connection.reddit

# Connect to Collection
stories = db.stories

# Drop Existing Collection
stories.drop()

# Get the reddit home page
reddit_page = urlopen("http://www.reddit.com/r/technology/.json")

# Parse the json into python objects
parsed = json.loads(reddit_page.read())

# iterate through every news item on the page
for item in parsed['data']['children']:
    # put it in mongo
    stories.insert_one(item['data'])
