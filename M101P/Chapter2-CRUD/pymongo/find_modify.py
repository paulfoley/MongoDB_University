## Example of using Find and then Modifying wiht pymongo

# Imports
import pymongo

# Connect to Mongo
connection = pymongo.MongoClient("mongodb://localhost")

# Connect to Database
db = connection.test

# Connect to Collection
counters = db.counters

def get_next_sequence_number(name):
    # let's get ourselves a sequence number
    # note there are two other varients of this call as well:
    # find_one_and_delete
    # find_one_and_replace
    # all these map to the the command find_and_modify

    # Exception Handling
    try: 
        # Find
        counter = counters.find_one_and_update(filter={'type':name}, update={'$inc':{'value':1}}, upsert=True, return_document=pymongo.ReturnDocument.AFTER)
        
        # Modify
        counter_value = counter['value']

        # Output
        return counter_value
    
    except Exception as e:
        print("Exception: ", type(e), e)

print(get_next_sequence_number('uid'))
print(get_next_sequence_number('uid'))
print(get_next_sequence_number('uid'))
