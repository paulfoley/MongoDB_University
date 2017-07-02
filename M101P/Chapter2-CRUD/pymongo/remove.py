## Example of Removing data with pymongo

# Imports
import pymongo
import datetime
import sys

# Connect to Mongo
connection = pymongo.MongoClient("mongodb://localhost")

# Connect to Database
db=connection.school

# Connect to Collection
scores = db.scores

# removes one student
def remove_student(student_id):
    # Removes one student using Delete Many (.delete_many())
    # Exception Handling
    try:
        # Get the Result
        result = scores.delete_many({'student_id':student_id})

        # Output
        print("num removed: ", result.deleted_count)

    except Exception as e:
        print ("Exception: ", type(e), e)

def find_student_data(student_id):
    # Find Student Data
    print("Searching for student data for student with id = ", student_id)

    # Exception Handling
    try: 
        # Output
        docs = scores.find({'student_id':student_id})
        for doc in docs:
            print(doc)

    except Exception as e:
        print("Exception: ", type(e), e)

remove_student(1)
find_student_data(1)
