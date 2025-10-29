# api/index.py
from flask import Flask, jsonify, abort
from flask_cors import CORS


app = Flask(__name__)
CORS(app, origins=["http://localhost:5173/mlc/Surprise", "https://dndnylah.github.io/mlc/Surprise", "https://dndnylah.github.io/mlc/", "https://dndnylah.github.io"])


movies = [
    {"id": 0, "title": "Interstellar", "form": "film", "platform": "rent", "status": "watched"},
    {"id": 1, "title": "Minding The Gap", "form": "film", "platform": "hulu", "status": "unwatched"},
    {"id": 2, "title": "Honey", "form": "film", "platform": "youtube", "status": "unwatched"},
    {"id": 3, "title": "Honey 2", "form": "film", "platform": "youtube", "status": "unwatched"},
    {"id": 4, "title": "Honey 3", "form": "film", "platform": "youtube", "status": "unwatched"},
    {"id": 5, "title": "Honey 4", "form": "film", "platform": "youtube", "status": "unwatched"},
    {"id": 6, "title": "Girlfriends", "form": "series", "platform": "netflix", "status": "unwatched"},
    {"id": 7, "title": "Steven Universe", "form": "series", "platform": "disney", "status": "unwatched"},
    {"id": 8, "title": "Howl's Movie Castle", "form": "film", "platform": "rent", "status": "unwatched"},
    {"id": 9, "title": "Kiki's Delivery Service", "form": "film", "platform": "rent", "status": "unwatched"},
    {"id": 11, "title": "Ponyo", "form": "film", "platform": "rent", "status": "unwatched"},
    {"id": 12, "title": "My Neighbor Totoro", "form": "film", "platform": "rent", "status": "unwatched"},
    {"id": 13, "title": "The Mask", "form": "film", "platform": "rent", "status": "unwatched"},
    {"id": 14, "title": "Weak Hero Class One", "form": "Series", "platform": "netflix", "status": "unwatched"},
    {"id": 15, "title": "Weak Hero Class Two", "form": "Series", "platform": "netflix", "status": "unwatched"},
    {"id": 16, "title": "Lemonade Mouth", "form": "film", "platform": "disney", "status": "unwatched"},
    {"id": 17, "title": "Harry Potter 4-9", "form": "film", "platform": "rent", "status": "unwatched"},
    {"id": 18, "title": "The Perks of Being a Wallflower", "form": "film", "platform": "rent", "status": "watched"},
    {"id": 19, "title": "Inception", "form": "film", "platform": "rent", "status": "unwatched"},
    {"id": 20, "title": "H2O", "form": "series", "platform": "netflix", "status": "unwatched"},
    {"id": 21, "title": "Baby Driver", "form": "film", "platform": "netflix", "status": "unwatched"},
    {"id": 22, "title": "Atypical", "form": "series", "platform": "netflix", "status": "unwatched"},
    {"id": 23, "title": "Living Single", "form": "series", "platform": "disney", "status": "unwatched"},
    {"id": 24, "title": "Love Rosie", "form": "film", "platform": "rent", "status": "unwatched"},
    {"id": 25, "title": "Love & Basketball", "form": "film", "platform": "rent", "status": "unwatched"},
    {"id": 26, "title": "The Goofy Movie", "form": "film", "platform": "disney", "status": "unwatched"},
    {"id": 27, "title": "Nope", "form": "film", "platform": "youtube", "status": "unwatched"},
    {"id": 28, "title": "The Italian Job", "form": "film", "platform": "rent", "status": "unwatched"},
    {"id": 29, "title": "The Assessment", "form": "film", "platform": "hulu", "status": "unwatched"},
    {"id": 30, "title": "Dark", "form": "series", "platform": "netflix", "status": "began"},
    {"id": 31, "title": "Wayward", "form": "series", "platform": "netflix", "status": "unwatched"},

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
