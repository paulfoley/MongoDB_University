## Using Find (.find()) through pymongo

# Import Pymongo
import pymongo
# It is not necessary to import sys

# Connect to the Database
connection = pymongo.MongoClient("mongodb://localhost")

# Connect to the "school" database
db = connection.school

# Connect to the "scores" collections
scores = db.scores


def find():
    # Function to find a list of 10 exams

    #Query
    print ("find, reporting for duty")
    query = {'type': 'exam'}

    # Exception Handling
    try:
        # Create Cursor
        cursor = scores.find(query)

    except Exception as e:
        # Print Error
        print ("Unexpected error:", type(e), e)

    # Sanity Score
    sanity = 0
    for single_doc in cursor:
        print (single_doc)
        sanity += 1
        if (sanity > 10):
            break


def find_one():
    # Function to find the first entry where student_id = 10

    # Query
    print ("find_one, reporting for duty")
    query = {'student_id': 10}
    
    # Exception Handling
    try:
        single_doc = scores.find_one(query)
        
    except Exception as e:
        print("Unexpected error:", type(e), e)
    
    print(single_doc)


if __name__ == '__main__':
    find()  # Change this to find_one() to run that function, instead.