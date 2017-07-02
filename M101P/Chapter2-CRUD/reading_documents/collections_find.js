// Example of Query's using .find() on Collections

db.movieDetails.find({rated: "PG-13" } ).pretty()
db.movieDetails.find({rated: "PG-13" } ).count()
db.movieDetails.find({rated: "PG-13", year: 2009 } ).count()
db.movieDetails.find({"tomato.meter": 100}).count()
db.movieDetails.find({"tomato.meter": 100}).pretty()
db.movieDetails.find({"writers": ["Ethan Coen", "Joel Coen"]}).count() // Count = 1
db.movieDetails.find({"writers": ["Ethan Coen", "Joel Coen"]}).pretty()
db.movieDetails.find({"writers": ["Joel Coen", "Ethan Coen"]}).count() // Count = 0
db.movieDetails.find({"actors": "Jeff Bridges"}).pretty()
db.movieDetails.find({"actors": "Jeff Bridges"}).count() // Count = 4
db.movieDetails.find({"actors.0": "Jeff Bridges"}).pretty()
db.movieDetails.find({"actors.0": "Jeff Bridges"}).count() // Count = 2	
db.movieDetails.find({rated: "PG"}).count() // Count = 108 more then batch size
var c = db.movieDetails.find() // Creates a cursor variable for the query
var doc = function() {
	return c.hasNext() ? c.next() : null;
}
db.movieDetails.find({rated: "PG"}, {title: 1}).pretty() // Projections only show certain info
db.movieDetails.find({rated: "PG"}, {title: 1, _id: 0}).pretty() // To exclude _id field put 0
db.movieDetails.find({rated: "PG"}, { writers: 0, actors: 0, _id: 0}).pretty() // Another example of excluding fields