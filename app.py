import os
import pickle
import streamlit as st
import pandas as pd
import urllib.request

# --- DOWNLOAD FILES IF MISSING ---
def download_if_missing(filename, url):
    if not os.path.exists(filename):
        gdrive_url = f"https://drive.google.com/uc?export=download&id={url.split('/d/')[1].split('/')[0]}"
        urllib.request.urlretrieve(gdrive_url, filename)

# Download files only if not present
download_if_missing("similarity.pkl", "https://drive.google.com/file/d/173GZwn0bqnQyNpV_Afj2o4xuj_u0zzzI/view?usp=drive_link")
download_if_missing("tmdb_5000_credits.csv", "https://drive.google.com/file/d/1j4FCtsw69CjshbyYHVAnfBRCMM4uYh4r/view?usp=drive_link")

# --- LOAD FILES ---
# Load the movies data from the CSV file
movies = pd.read_csv('tmdb_5000_credits.csv')

# Load the similarity matrix
similarity = pickle.load(open('similarity.pkl', 'rb'))

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

# Populate the list of movie titles
movie_list = movies['title'].values
selected_movie = st.selectbox("Select a movie to get recommendations:", movie_list)

if st.button('Recommend'):
    recommendations = recommend(selected_movie)
    st.subheader("Top 5 Recommendations:")
    for movie in recommendations:
        st.markdown(f'<div class="movie-box">{movie}</div>', unsafe_allow_html=True)
