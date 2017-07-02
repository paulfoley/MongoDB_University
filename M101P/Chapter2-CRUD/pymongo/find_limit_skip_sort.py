## Example of using 1)Sort(.sort()) 2)Skip(.skip()) 3)Limit (.limit())in Pymongo

# Imports
import pymongo

# Connect to Mongo
connection = pymongo.MongoClient("mongodb://localhost")

# Connect to Database
db = connection.school

# Connect to Collection
scores = db.scores


def find():
    # Program using 1)Sort 2)Skip 3)Limit
    print ("find, reporting for duty")

    # Query
    query = {}

    # Exception Handling
    try:
        # Create Cursor 

        # Out of order returns the same result
        #cursor = scores.find(query).skip(4)
        #cursor.limit(1)
        #cursor.sort([('student_id', pymongo.ASCENDING), ('score', pymongo.DESCENDING)])
        
        # In order returns the same result
        cursor = scores.find(query)
        cursor.sort([('student_id', pymongo.ASCENDING), ('score', pymongo.DESCENDING)]).skip(4).limit(1)
    
    except Exception as e:
        print("Unexpected error:", type(e), e)

    # Outpu
    for doc in cursor:
        print (doc)


if __name__ == '__main__':
    find()
