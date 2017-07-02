## Example of Update using Set with in pymongo

# Imports
import pymongo
import datetime

# Connect to Mongo
connection = pymongo.MongoClient("mongodb://localhost")

# Connect to Database
db = connection.school

# Connect to Collections
scores = db.scores

def add_review_date_using_update_one(student_id):
    # Update One (.update_one()) using Set ($set)
    print("updating record using update_one and $set")

    # Error Handling
    try:
        # Get the Score
        score = scores.find_one({'student_id': student_id, 'type': 'homework'})
        print ("before: ", score)

        # Update One using Set
        record_id = score['_id']
        result = scores.update_one({'_id': record_id}, {'$set': {'review_date': datetime.datetime.utcnow()}})
        print("num matched: ", result.matched_count)

        # Output
        score = scores.find_one({'_id': record_id})
        print("after: ", score)

    except Exception:
        raise


def add_review_dates_for_all():
    # Update Many (.update_many()) using Set($set)
    print("updating record using update_many and $set")

    # Exception Handling
    try:
        # Update Many using Set
        result = scores.update_many({}, {'$set': {'review_date': datetime.datetime.utcnow()}})
        
        # Output
        print("num matched: ", result.matched_count)

    except Exception:
        raise

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

if __name__ == '__main__':
    #add_review_date_using_update_one(1)
    add_review_dates_for_all()
    #remove_all_review_dates()
