from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import os
import gdown
import pandas as pd

app = Flask(__name__)
CORS(app)

# Google Drive file ID for similarity.pkl
SIMILARITY_FILE_ID = "YOUR_FILE_ID_HERE"
SIMILARITY_PATH = "similarity.pkl"
MOVIES_PATH = "movies.pkl"

# Download similarity.pkl if not present
if not os.path.exists(SIMILARITY_PATH):
    print("🔄 Downloading similarity.pkl from Google Drive...")
    gdown.download(f"https://drive.google.com/uc?id={SIMILARITY_FILE_ID}", SIMILARITY_PATH, quiet=False)

# Load required files
movies = pickle.load(open(MOVIES_PATH, 'rb'))
similarity = pickle.load(open(SIMILARITY_PATH, 'rb'))

@app.route('/')
def home():
    return "✅ Backend is running!"

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    movie_name = data.get('movie', "").lower()

    movie_list = movies['title'].str.lower().tolist()
    if movie_name not in movie_list:
        return jsonify({'recommended_movies': []}), 404

    index = movie_list.index(movie_name)
    distances = list(enumerate(similarity[index]))
    movies_sorted = sorted(distances, key=lambda x: x[1], reverse=True)[1:6]

    recommended_movies = [movies.iloc[i[0]].title for i in movies_sorted]
    return jsonify({'recommended_movies': recommended_movies})

if __name__ == '__main__':
    app.run(debug=True)
