from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import pandas as pd
import requests
import os

app = Flask(__name__)
CORS(app)

# Load movies.pkl locally
movies = pickle.load(open('movies.pkl', 'rb'))

# Download and load similarity.pkl from Google Drive
SIMILARITY_PICKLE_URL = "https://drive.google.com/uc?id=1WQs0UfDCdmtBHe74y1z571kAGIm-ogp2"
SIMILARITY_FILE = "similarity.pkl"

def download_similarity():
    if not os.path.exists(SIMILARITY_FILE):
        print("📥 Downloading similarity.pkl...")
        r = requests.get(SIMILARITY_PICKLE_URL)
        with open(SIMILARITY_FILE, 'wb') as f:
            f.write(r.content)

download_similarity()
similarity = pickle.load(open(SIMILARITY_FILE, 'rb'))

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
