## Example of using Greater Then ($gt) and Less Then ($lt) in pymongo

# Imports
import pymongo

# Connect to the Database
connection = pymongo.MongoClient("mongodb://localhost")

# Connect to the "school" database
db = connection.school

# Connect to the "score" Collection
scores = db.scores


def find():
    # Find statement with Greater Then ($gt) and ($lt)
    print ("find, reporting for duty")

    # Query
    query = {'type': 'exam', 'score': {'$gt': 50, '$lt': 70}}

    # Projection
    projection = {"student_id": 1, "score": 1, "_id": 0}

    # Exception Handling
    try:
        cursor = scores.find(query, projection)

    except Exception as e:
        print ("Unexpected error:", type(e), e)

    # Output
    sanity = 0
    for doc in cursor:
        print (doc)
        sanity += 1
        if (sanity > 10):
            break


if __name__ == '__main__':
    find()
