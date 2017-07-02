// Regular Expression ($regex) Queries
db.movieDetails.find({}, {"awards.text": 1, _id: 0}).pretty()
db.movieDetails.find({"awards.text": {$regex: /^Won.*/}}).count()
db.movieDetails.find({"awards.text": {$regex: /^Won.*/}}, {title: 1, "awards": 1, _id: 0}).pretty()
