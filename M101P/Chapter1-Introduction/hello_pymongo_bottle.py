import bottle
import pymongo

# this is the handler for the default path of the web server
@bottle.route('/')
def index():
    # connect to mongoDB
    connection = pymongo.MongoClient('localhost', 27017)

    # attach to test database
    db = connection.test

    # find a single document
    item = db.names.find_one()
    return '<b>Hello %s!</b>' % item['name']


bottle.run(host='localhost', port=8082)
