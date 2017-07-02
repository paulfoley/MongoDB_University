## Example of Upsert in pymongo

# Imports
import pymongo
import sys

# Connect to Mongo
connection = pymongo.MongoClient("mongodb://localhost")

# Connect to the Database
db = connection.test

# Connect to the Collection
things = db.things

def using_upsert():
    # Inserting using Update & Replace with Upserts
    print("updating with upsert")

    # Exception Handling
    try:
        # Remove all stuff from Things collection
        things.drop()

        # Adding things with Update and Upsert
        things.update_one({'thing':'apple'}, {'$set':{'color':'red'}}, upsert=True)
        things.update_many({'thing':'banana'}, {'$set':{'color':'yellow'}}, upsert=True)
        
        # Example with Replace and Upsert
        things.replace_one({'thing':'pear'}, {'color':'green'}, upsert=True)
        # As {'thing':'pear'} is in the filter field it doesn't get added BUT {'color':'green'} does as it's in the update field

        # Output
        apple = things.find_one({'thing':'apple'})
        print("apple: ", apple)
        banana = things.find_one({'thing':'banana'})
        print("banana: ", banana)
        pear = things.find_one({'thing':'pear'})
        print("pear: ", pear)

    except Exception as e:
        print("Unexpected error:", type(e), e)
        raise

using_upsert()
