## Example of Insert_One in pymongo

# Imports
import pymongo

# Connect to Mongo
connection = pymongo.MongoClient("mongodb://localhost")

# Connect to Database
db = connection.school

# Connect to Collection
people = db.people

def insert_two():
    # Insert two persons into the people collection
    print("insert, reporting for duty")

    # People
    richard = {"name": "Richard Kreuter", "company": "MongoDB", "interests": ['horses', 'skydiving', 'fencing']}
    andrew = {"_id": "erlichson", "name": "Andrew Erlichson", "company": "MongoDB", "interests": ['running', 'cycling', 'photography']}
    
    # Exception Handling
    try:
        people.insert_one(richard)
        people.insert_one(andrew)

    except Exception as e:
        print("Unexpected error:", type(e), e)

    print(richard)
    print(andrew)


if __name__ == '__main__':
    insert_two()
