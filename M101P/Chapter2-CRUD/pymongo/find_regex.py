## Example of using Regular Expressions in Mongo

# Imports
import pymongo

# Connect to Mongo
connection = pymongo.MongoClient("mongodb://localhost")

# Connect to Database
db = connection.reddit

# Connect to Collection
stories = db.stories


def find():
    # Find using Regular Expression
    print ("find, reporting for duty")

    # Query
    query = {'title': {'$regex': 'apple|google', '$options': 'i'}}
    
    # Projection
    projection = {'title': 1, '_id': 0}

    # Exception Handling
    try:
        cursor = stories.find(query, projection)

    except Exception as e:
        print ("Unexpected error:", type(e), e)

    # Output
    for doc in cursor:
        print (doc)

if __name__ == '__main__':
    find()
