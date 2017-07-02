## Example of using Insert Many and highlighting order

# Improts
import pymongo

# Connect to Mongo
connection = pymongo.MongoClient("mongodb://localhost")

# Connect to Database
db = connection.school

# Connect to Collection
people = db.people

def insert_many():
    # Insert Multiple People at Once

    # People
    print("insert_many, reporting for duty")
    andrew = {"_id": "erlichson", "name": "Andrew Erlichson",
              "company": "MongoDB",
              "interests": ['running', 'cycling', 'photography']}
    richard = {"name": "Richard Kreuter", "company": "MongoDB",
               "interests": ['horses', 'skydiving', 'fencing']}
    people_to_insert = [andrew, richard]

    # Exception Handling
    try:
        people.insert_many(people_to_insert, ordered=False)
    
    except Exception as e:
        print ("Unexpected error:", type(e), e)


def print_people():
    # Function to print People

    # Create the Cursor
    cursor = people.find({}, {'name': 1})
    
    # Output
    for doc in cursor:
        print (doc)

if __name__ == '__main__':
    print("Before the insert_many, here are the people")
    print_people()
    insert_many()
    print("\n\nAfter the insert_many, here are the people")
    print_people()
