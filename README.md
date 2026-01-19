🎬 Movie Recommendation System

A content-based movie recommendation system built using the TMDB 5000 Movie Dataset.
The application recommends similar movies based on genres, cast, crew, and keywords using Natural Language Processing (NLP) and cosine similarity.

This is a full-stack web application with:

ReactJS as the frontend

Flask as the backend

A precomputed similarity matrix for fast recommendations

🚀 Features

Content-based movie recommendations

NLP-driven feature extraction (genres, cast, crew, keywords)

Vectorization using CountVectorizer

Similarity computation using Cosine Similarity

Fast responses using a pre-trained similarity matrix

Clean React UI with real-time API interaction

RESTful Flask backend

🧠 How It Works

Movie metadata is preprocessed and combined into a single text feature

Text is vectorized using CountVectorizer

Cosine similarity is computed between all movies

Similarity matrix is saved as similarity.pkl

User selects a movie → backend returns top similar movies

React frontend displays recommendations

🧰 Tech Stack
Frontend

ReactJS

Axios

CSS

Backend

Flask

Flask-CORS

Pandas

Pickle

Machine Learning / NLP

Scikit-learn

CountVectorizer

Cosine Similarity

Stemming

ast.literal_eval

📂 Project Structure
movie-recommendation-system/
│
├── backend/
│   ├── app.py
│   ├── movies.pkl
│   ├── similarity.pkl
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│
└── README.md

▶️ Running the Project Locally
1️⃣ Backend (Flask)
cd backend
python app.py


Backend runs on:

http://127.0.0.1:5000

2️⃣ Frontend (React)
cd frontend
npm install
npm start


Frontend runs on:

http://localhost:3000

📦 Dataset & Model Files

Dataset: TMDB 5000 Movies Dataset

Precomputed Similarity Matrix:
👉 Download similarity.pkl

⚠️ Place similarity.pkl inside the backend folder before running the app.

🔗 Project Links

Frontend Repository:
https://github.com/akshatbuliwal/movie-recommendation-system-frontend

📌 Future Improvements

Fuzzy search for partial movie names

Autocomplete dropdown for movie selection

User-based collaborative filtering

UI enhancements and loading states

Deployment with environment-based configuration

🙌 Author

Akshat Buliwal
Full-Stack & Machine Learning Enthusiast
