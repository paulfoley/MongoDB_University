// all Query
db.movieDetails.find({genres: {$all: ["Comedy", "Crime", "Drama"]}}).count()
db.movieDetails.find({genres: {$all: ["Comedy", "Crime", "Drama"]}}, {title: 1, genres: 1, _id: 0}).pretty()

// size Query
db.movieDetails.find({countries: {$size: 1}}).count()
db.movieDetails.find({countries: {$size: 1}}, {title: 1, countries: 1, _id: 0}).pretty()

// Match a certain value in the array (In this case the 2nd value)
db.movieDetails.find({"countries.1": "Sweden"}, {title: 1, countries: 1, _id: 0}).count()
db.movieDetails.find({"countries.1": "Sweden"}, {title: 1, countries: 1, _id: 0}).pretty()

// elemMatch Query
db.movieDetails.find({boxOffice: {$elemMatch: {country: "UK", revenue: {$gt: 15}}}}).count()
db.movieDetails.find({boxOffice: {$elemMatch: {country: "UK", revenue: {$gt: 15}}}}, {title: 1, country: 1, _id: 0}).pretty()

boxOffice: [{"country": "USA", "revenue": 41.3}, {"country": "Australia", "revenue": 2.9}, {"country": "UK", "revenue": 10.1}, {"country": "Germany", "revenue": 4.3}, {"country": "France", "revenue": 3.5}]

