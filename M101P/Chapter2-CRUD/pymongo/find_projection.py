## Example of using Projections

# Imports
import pymongo
import sys

# Connect to the Client
connection = pymongo.MongoClient("mongodb://localhost")

# Connect to the Database
db = connection.school

# Connect to the Collections
scores = db.scores


def find():
    # Function using Find with Projections
    print ("find, reporting for duty")

    # Query
    query = {'type': 'exam'}

    # Projection
    projection = {'student_id': 1, '_id': 0}
    
    # Error Handling
    try:
        cursor = scores.find(query, projection)

    except Exception as e:
        print ("Unexpected error:", type(e), e)

    # Function    
    sanity = 0
    for doc in cursor:
        print (doc)
        sanity += 1
        if (sanity > 10):
            break


if __name__ == '__main__':
    find()
