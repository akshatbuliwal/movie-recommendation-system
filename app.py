from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import pandas as pd
import requests

app = Flask(__name__)
CORS(app)

# Load movies.pkl
with open('movies.pkl', 'rb') as f:
    movies = pickle.load(f)

# Download similarity.pkl from Google Drive
def download_similarity_file():
    file_id = "1WQs0UfDCdmtBHe74y1z571kAGIm-ogp2"
    url = f"https://drive.google.com/uc?export=download&id={file_id}"
    response = requests.get(url)
    with open("similarity.pkl", "wb") as f:
        f.write(response.content)

# Check if similarity.pkl exists, otherwise download
try:
    with open('similarity.pkl', 'rb') as f:
        similarity = pickle.load(f)
except FileNotFoundError:
    download_similarity_file()
    with open('similarity.pkl', 'rb') as f:
        similarity = pickle.load(f)

@app.route('/')
def home():
    return "✅ Backend is run
