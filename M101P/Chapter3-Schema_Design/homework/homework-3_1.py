## Chapter 3 Homework 1

# Imports
import pymongo

# Connect to Mongo
connection = pymongo.MongoClient()

# Connect to Database
db = connection.school

# Connect to Collection
students = db.students

def find_lowest_hw(scores):
    # Finds lowest hw score in the list.
    lowest = None
    lowest_score = 101
    for item in scores:
        if ((item['type'] == "homework") and (item['score'] < lowest_score)):
            # found a new bound
            lowest = item
            lowest_score = lowest['score']
    return lowest

def remove_lowest():
    # Drops the lowest score for each student.
    cursor = students.find()
    for student in cursor:
        _id = student["_id"]
        scores = student['scores']
        lowest = find_lowest_hw(scores)
        if (lowest is not None):
            scores.remove(lowest)
            students.update_one({'_id': _id}, {'$set': {'scores': scores}})
        else:
            print("Could not find a homework score to process")

def main():
    print("Removing lowest score from students")
    remove_lowest()

if __name__ == '__main__':
    main()
