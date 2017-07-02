## Example using Mongo's GRIDFS functionality

#Imports
import pymongo
import gridfs

# Connect to Mongo
connection = pymongo.MongoClient()

# Connect to Database
db = connection.test

# Connect to Collection
file_meta = db.file_meta
file_used = "sample_128_mb.txt"

def main():
	# Use Mongo's GRIDFS
    grid = gridfs.GridFS(db, "text")
    fin = open(file_used, "r")
    _id = grid.put(fin)
    fin.close()
    #print("id of file is", _id)
    #file_meta.insert({"grid_id": _id, "filename": file_used})

if __name__ == '__main__':
    main()
