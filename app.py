from flask import Flask, jsonify, request

app = Flask(__name__)

movies = [
    {"id": 0, "title": "Interstellar", "type": "film", "platform": "rent", "status": "watched"},
    {"id": 1, "title": "Minding The Gap", "type": "film", "platform": "hulu", "status": "unwatched"},
    {"id": 2, "title": "Honey", "type": "film", "platform": "youtube", "status": "unwatched"},
    {"id": 3, "title": "Honey 2", "type": "film", "platform": "youtube", "status": "unwatched"},
    {"id": 4, "title": "Honey 3", "type": "film", "platform": "youtube", "status": "unwatched"},
    {"id": 5, "title": "Honey 4", "type": "film", "platform": "youtube", "status": "unwatched"},
    {"id": 6, "title": "Girlfriends", "type": "series", "platform": "netflix", "status": "unwatched"},
    {"id": 7, "title": "Steven Universe", "type": "series", "platform": "disney", "status": "unwatched"},
    {"id": 8, "title": "Howl's Movie Castle", "type": "film", "platform": "rent", "status": "unwatched"},
    {"id": 9, "title": "Kiki's Delivery Service", "type": "film", "platform": "rent", "status": "unwatched"},
    {"id": 11, "title": "Ponyo", "type": "film", "platform": "rent", "status": "unwatched"},
    {"id": 12, "title": "My Neighbor Totoro", "type": "film", "platform": "rent", "status": "unwatched"},
    {"id": 13, "title": "The Mask", "type": "film", "platform": "rent", "status": "unwatched"},
    {"id": 14, "title": "Weak Hero Class One", "type": "Series", "platform": "netflix", "status": "unwatched"},
    {"id": 15, "title": "Weak Hero Class Two", "type": "Series", "platform": "netflix", "status": "unwatched"},
    {"id": 16, "title": "Lemonade Mouth", "type": "film", "platform": "disney", "status": "unwatched"},
    {"id": 17, "title": "Harry Potter 4-9", "type": "film", "platform": "rent", "status": "unwatched"},
    {"id": 18, "title": "The Perks of Being a Wallflower", "type": "film", "platform": "rent", "status": "watched"},
    {"id": 19, "title": "Inception", "type": "film", "platform": "rent", "status": "unwatched"},
    {"id": 20, "title": "H2O", "type": "series", "platform": "netflix", "status": "unwatched"},
    {"id": 21, "title": "Baby Driver", "type": "film", "platform": "netflix", "status": "unwatched"},
    {"id": 22, "title": "Atypical", "type": "series", "platform": "netflix", "status": "unwatched"},
    {"id": 23, "title": "Living Single", "type": "series", "platform": "disney", "status": "unwatched"},
    {"id": 24, "title": "Love Rosie", "type": "film", "platform": "rent", "status": "unwatched"},
    {"id": 25, "title": "Love & Basketball", "type": "film", "platform": "rent", "status": "unwatched"},
    {"id": 26, "title": "The Goofy Movie", "type": "film", "platform": "disney", "status": "unwatched"},
]

# GET: Return all movies
@app.route('/api/movies', methods=['GET'])
def get_movies():
    return jsonify(movies)

# GET: Return a specific movie by ID
@app.route('/api/movies/<int:movie_id>', methods=['GET'])
def get_movie(movie_id):
    movie = next((m for m in movies if m['id'] == movie_id), None)
    return jsonify(movie) if movie else ('Not found', 404)

# POST: Add a new movie
@app.route('/api/movies', methods=['POST'])
def add_movie():
    data = request.get_json()
    new_movie = {
        "id": len(movies) + 1,
        "title": data['title'],
        "type": data['type'],
        "platform": data['platform'],
        "status": data['status']
    }
    movies.append(new_movie)
    return jsonify(new_movie), 201

if __name__ == '__main__':
    app.run(debug=True)