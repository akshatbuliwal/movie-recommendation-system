# 🎬 Movie Recommendation System

A **content-based movie recommendation system** built using the **TMDB 5000 Movie Dataset**.
The application recommends similar movies based on **genres, cast, crew, and keywords** using **Natural Language Processing (NLP)** and **cosine similarity**.

This is a **full-stack web application** with:

* **ReactJS** as the frontend
* **Flask** as the backend
* A **precomputed similarity matrix** for fast recommendations

---

## 🚀 Features

* Content-based movie recommendations
* NLP-driven feature extraction (genres, cast, crew, keywords)
* Vectorization using **CountVectorizer**
* Similarity computation using **Cosine Similarity**
* Fast responses using a pre-trained similarity matrix
* Clean React UI with real-time API interaction
* RESTful Flask backend

---

## 🧠 How It Works

* Movie metadata is preprocessed and combined into a single text feature
* Text is vectorized using **CountVectorizer**
* **Cosine similarity** is computed between all movies
* The similarity matrix is stored as `similarity.pkl`
* User selects a movie → backend returns the most similar movies
* React frontend displays the recommendations

---

## 🧰 Tech Stack

**Frontend**

* ReactJS
* Axios
* CSS

**Backend**

* Flask
* Flask-CORS
* Pandas
* Pickle

**Machine Learning / NLP**

* Scikit-learn
* CountVectorizer
* Cosine Similarity
* Stemming
* `ast.literal_eval`

---

## 🔗 Project Links

**Frontend Repository**
[https://github.com/akshatbuliwal/movie-recommendation-system-frontend](https://github.com/akshatbuliwal/movie-recommendation-system-frontend)

---

## 📌 Future Improvements

* Fuzzy search for partial movie names
* Autocomplete dropdown for movie selection
* User-based collaborative filtering
* UI enhancements and loading states
* Environment-based configuration for deployment

---

## 🙌 Author

**Akshat Buliwal**
Full-Stack & Machine Learning Enthusiast
