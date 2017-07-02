## Mongo Chapter 2 Homework 2

# Imports
import pymongo

# Connect to Mongo
connection = pymongo.MongoClient("mongodb://localhost")

# Connect to Database
db = connection.students

# Connect to Collection
grades = db.grades

def remove_score():
	# Query
	query = {"type":"homework"}
	projection = {"student_id":1, "score": 1}
	cursor = grades.find(query,projection)

	# Sort
	cursor.sort([('student_id',pymongo.ASCENDING), ('score',pymongo.DESCENDING)])

	# Output
	output = []
	for doc in cursor:
		output.append(doc)

	for i in range(1, len(output),2):
		o_id = output[i]['_id']
		result = grades.delete_many({'_id':o_id})

remove_score()