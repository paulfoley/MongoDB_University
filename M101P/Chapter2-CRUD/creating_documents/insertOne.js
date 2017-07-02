// Insert One without _id field defined
db.moviesScratch.insertOne({ "title": "Rocky", "year": "1976", "imdb": "tt0075148"});

// Insert One with _id field defined
db.moviesScratch.insertOne({ "_id": "tt0075148", "title": "Rocky", "year": "1976" });
