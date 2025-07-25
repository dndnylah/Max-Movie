# api/index.py
from flask import Flask, jsonify, abort
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

movies = [
    {"id": 0, "title": "Interstellar", "type": "film", "platform": "rent", "status": "watched"},
    {"id": 1, "title": "Minding The Gap", "type": "film", "platform": "hulu", "status": "unwatched"},
]

@app.route("/api/movies", methods=["GET"])
def get_movies():
    return jsonify(movies)

@app.route("/api/movies/<int:movie_id>", methods=["GET"])
def get_movie(movie_id):
    movie = next((m for m in movies if m["id"] == movie_id), None)
    if movie:
        return jsonify(movie)
    else:
        abort(404, description="Movie not found")
