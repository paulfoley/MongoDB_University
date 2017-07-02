## Example using Replace One (.replace_one()) with pymongo

# Imports
import pymongo
import datetime
import sys

# Connect to Mongo
connection = pymongo.MongoClient("mongodb://localhost")

# Connect to Database
db=connection.school

# Connect to Collections
scores = db.scores

def remove_all_review_dates():
    # Removes all review dates using Update Many (.update_many()) with Unset ($unset)
    print("\n\nremoving all review dates")

    # Exception Handling
    try:
        result = scores.update_many({'review_date':{'$exists':True}}, {'$unset':{'review_date':1}})
        print("Matched this number of docs: ", result.matched_count)

    except Exception as e:
        print("Unexpected error:", type(e), e)
        raise

def add_review_date_using_replace_one(student_id):
    # Add a review date to single record using Replace One (.replace_one())
    print("updating record using replace_one")

    # Exception Handling
    try:
        # Get the Score
        score = scores.find_one({'student_id':student_id, 'type':'homework'})
        print("before: ", score)

        # Add a review_date
        score['review_date'] = datetime.datetime.utcnow()

        # Update the record with Replace One
        record_id = score['_id']
        scores.replace_one({'_id': record_id}, score)
        score = scores.find_one({'_id': record_id})
        
        # Output
        print("after: ", score)

    except Exception as e:
        print("Unexpected error:", type(e), e)
        raise

remove_all_review_dates()
add_review_date_using_replace_one(1)

