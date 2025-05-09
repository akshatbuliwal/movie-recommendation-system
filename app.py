import os
import pickle
import streamlit as st
import pandas as pd
import urllib.request

# --- DOWNLOAD FILES IF MISSING ---
def download_if_missing(filename, gdrive_file_id):
    if not os.path.exists(filename):
        download_url = f"https://drive.google.com/uc?export=download&id={gdrive_file_id}"
        try:
            urllib.request.urlretrieve(download_url, filename)
            print(f"Downloaded: {filename}")
        except Exception as e:
            print(f"Failed to download {filename}: {e}")

# --- DOWNLOAD FILES ---
download_if_missing("similarity.pkl", "173GZwn0bqnQyNpV_Afj2o4xuj_u0zzzI")
download_if_missing("movies.pkl", "1jfFLU0ZP3uUguMCKjIri9m_MIfvnkxRA")

# --- LOAD FILES ---
with open("movies.pkl", "rb") as f:
    movies = pickle.load(f)

with open("similarity.pkl", "rb") as f:
    similarity = pickle.load(f)

# --- RECOMMENDER FUNCTION ---
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    return [movies.iloc[i[0]].title for i in movie_list]

# --- STREAMLIT UI CONFIG ---
st.set_page_config(page_title="Movie Recommender", page_icon="🎬", layout="centered")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .title {
        font-size: 40px;
        font-weight: bold;
        color: #4a4a4a;
        text-align: center;
        margin-bottom: 30px;
    }
    .movie-box {
        background-color: #e0f7fa;
        padding: 10px 20px;
        margin: 10px 0;
        border-radius: 8px;
        color: #006064;
        font-size: 18px;
        font-weight: 500;
    }
    </style>
""", unsafe_allow_html=True)

# --- UI ---
st.markdown('<div class="title">🎥 Movie Recommender System</div>', unsafe_allow_html=True)

movie_list = movies['title'].values
selected_movie = st.selectbox("Select a movie to get recommendations:", movie_list)

if st.button('Recommend'):
    recommendations = recommend(selected_movie)
    st.subheader("Top 5 Recommendations:")
    for movie in recommendations:
        st.markdown(f'<div class="movie-box">{movie}</div>', unsafe_allow_html=True)
