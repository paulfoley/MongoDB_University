// Greater Then ($gt) Queries
db.movieDetails.find({runtime:{ $gt: 90 } }).count()
db.movieDetails.find({runtime:{$gt: 90}}).pretty()
db.movieDetails.find({runtime:{$gt: 90}}, {title : 1, runtime: 1, _id : 0}).pretty()

// Greater Then or Equal To ($gte) and Less Then or Equal To ($lte) Queries
db.movieDetails.find({runtime:{$gte: 90, $lte: 120}}).count()
db.movieDetails.find({runtime:{$gte: 90, $lte: 120}}, {title: 1, runtime: 1, _id: 0}).pretty()

// Greater Then or Equalt To ($gte) and Greater Then ($gt) Queries
db.movieDetails.find({"tomato.meter": {$gte: 95}, runtime: {$gt: 180}}).count()
db.movieDetails.find({"tomato.meter": {$gte: 95}, runtime: {$gt: 180}}, {title: 1, runtime: 1, _id: 0}).pretty()

// Not Equal To ($ne) Queries
db.movieDetails.find({rated: {$ne: "UNRATED"}}, {title: 1, rated: 1, _id: 0}).pretty()
db.movieDetails.find({rated: {$ne: "UNRATED" }}).count()

// In ($in) Queries
db.movieDetails.find({rated: {$in: ["G", "PG", "PG-13"]}}, {title: 1, rated: 1, _id: 0}).pretty()
db.movieDetails.find({rated: {$in: ["G", "PG"]}}).count()
