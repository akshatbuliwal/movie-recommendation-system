import streamlit as st
import pickle
import pandas as pd

# Page config
st.set_page_config(page_title="Movie Recommender", page_icon="🎬", layout="centered")

# Load saved data
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Recommender function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended = [movies.iloc[i[0]].title for i in movie_list]
    return recommended

# Inject custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #f7f7f7;
    }
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

# UI
st.markdown('<div class="title">🎥 Movie Recommender System</div>', unsafe_allow_html=True)

movie_list = movies['title'].values
selected_movie = st.selectbox(
    'Select a movie to get recommendations:',
    movie_list,
    key="movie_dropdown"
)

if st.button('Recommend'):
    recommendations = recommend(selected_movie)
    st.subheader("Top 5 Recommendations:")
    for movie in recommendations:
        st.markdown(f'<div class="movie-box">{movie}</div>', unsafe_allow_html=True)
