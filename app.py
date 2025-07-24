from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import os
import gdown  # make sure to install this in your requirements.txt

app = Flask(__name__)
CORS(app)

# ✅ Step 1: Check if similarity.pkl exists, else download
SIMILARITY_FILE = "similarity.pkl"
DRIVE_ID = "1WQs0UfDCdmtBHe74y1z571kAGIm-ogp2"
DRIVE_URL = f"https://drive.google.com/uc?id={DRIVE_ID}"

if not os.path.exists(SIMILARITY_FILE):
    print("📥 similarity.pkl not found locally. Downloading from Google Drive...")
    gdown.download(DRIVE_URL, SIMILARITY_FILE, quiet=False)

# ✅ Step 2: Load the data files
print("📦 Loading pickle files...")
movies = pickle.load(open("movies.pkl", "rb"))
similarity = pickle.load(open(SIMILARITY_FILE, "rb"))

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    movie = data.get('movie')

    print(f"\n🎬 Received input movie: {movie}")

    if not movie or movie.strip() == "":
        print("⚠️ No movie name provided")
        return jsonify({'error': 'No movie name provided'}), 400

    movie = movie.strip().lower()
    titles = movies['title'].str.lower()

    if movie not in titles.values:
        print("❌ Movie not found in dataset")
        return jsonify({'recommended_movies': []}), 200

    index = titles[titles == movie].index[0]
    distances = list(enumerate(similarity[index]))
    distances = sorted(distances, reverse=True, key=lambda x: x[1])[1:6]

    recommendations = [movies.iloc[i[0]].title for i in distances]
    print(f"✅ Recommended movies: {recommendations}")

    return jsonify({'recommended_movies': recommendations})

if __name__ == '__main__':
    app.run(debug=True)
