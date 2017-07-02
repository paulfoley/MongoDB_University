// Or ($or) Queries
db.movieDetails.find({$or: [{"tomato.meter": {$gt: 95}}, {"metacritic": {$gt: 88}}]}).count()
db.movieDetails.find({$or: [{"tomato.meter": {$gt: 95}}, {"metacritic": {$gt: 88}}]}, {title: 1, "tomato.meter": 1, "metacritic": 1, _id: 0}).pretty()

// And ($and) Queries
db.movieDetails.find({$and: [{"tomato.meter": {$gt: 95}}, {"metacritic": {$gt: 88}}]}).count()
db.movieDetails.find({$and: [{"tomato.meter": {$gt: 95}}, {"metacritic": {$gt: 88}}]}, {title: 1, "tomato.meter": 1, "metacritic": 1, _id: 0}).pretty()
db.movieDetails.find({$and: [{"metacritic": {$ne: null}}, {"metacritic": {$exists: true}}]}).count()
db.movieDetails.find({$and: [{"metacritic": {$ne: null}}, {"metacritic": {$exists: true}}]}, {title: 1, "metacritic": 1, _id: 0}).pretty()
