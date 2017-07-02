## Mongo Chapter 2 Homework 1

# Imports
import pymongo

# Connect to Mongo
connection = pymongo.MongoClient("mongodb://localhost")

# Connect to Database
db = connection.students

# Connect to Collection
grades = db.grades

def greater_then():
	# Query
	query = {"score": {"$gte": 65}}
	cursor = grades.find(query)

	# Sort
	cursor.sort("score", pymongo.DESCENDING)

	# Output
	for doc in cursor:
		print(doc)

greater_then()
