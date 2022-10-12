from pymongo import MongoClient

# Requires the PyMongo package.
# https://api.mongodb.com/python/current

client = MongoClient('mongodb://localhost:27017/?readPreference=primary&appname=MongoDB+Compass&directConnection=true&ssl=false')
result = client['a']['us'].aggregate([
    {
        '$project': {
            '_id': '$id', 
            'first_name': 1, 
            'last_name': 1, 
            'email': 1
        }
    }, {
        '$out': 'x'
    }
])