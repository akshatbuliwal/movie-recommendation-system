from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)

# Load required files
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

@app.route('/')
def home():
    return "✅ Backend is running!"

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    movie_name = data.get('movie', "").lower()

    # Normalize movie titles
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
