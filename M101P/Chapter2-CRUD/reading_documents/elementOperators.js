// Exists ($exists) Queries - Matches documents that have the specified field.
db.movieDetails.find({"tomato.meter": {$exists: true}}).count()
db.movieDetails.find({"tomato.meter": {$exists: true}}, {title: 1, "tomato.meter": 1, _id: 0}).pretty()
db.movieDetails.find({"tomato.meter": {$exists: false}}).count()
db.movieDetails.find({"tomato.meter": {$exists: false}}, {title: 1, "tomato.meter": 1, _id: 0}).pretty()

// Type ($type) Queries - Selects documents if a field is of the specified type.
db.moviesScratch.find({_id: {$type: "string"}}).count()
db.moviesScratch.find({_id: {$type: "string"}}, {_id: 1}).pretty()
