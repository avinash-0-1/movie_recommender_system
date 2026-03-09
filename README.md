# 🎬 Movie Recommender System

A content-based **Movie Recommendation System** built using **Python** and deployed with **Streamlit**. The application suggests movies similar to the one selected by the user by analyzing movie metadata and computing similarity between movies.

---

## 🚀 Live Demo

🔗 **Try the app here:**  
https://avinash-0-1-movie-recommender-system-app-ndwvve.streamlit.app/

---

## 🚀 Features

- Recommend movies based on similarity
- Content-based filtering approach
- Interactive web interface using Streamlit
- Displays movie posters using TMDB API
- Fast and simple recommendation system

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- TMDB API

---

## 📂 Project Structure

```
movie-recommender-system
│
├── app.py
├── movies.pkl
├── similarity.pkl
├── requirements.txt
└── README.md
```

---

## ⚙️ How It Works

1. The movie dataset is preprocessed to extract important features such as genres, keywords, cast, and crew.
2. These features are combined into a single textual format.
3. Text data is converted into vectors using vectorization techniques.
4. Cosine similarity is calculated between movie vectors.
5. When a user selects a movie, the system recommends the most similar movies.

---

## ▶️ Run Locally

### Clone the repository

```
git clone https://github.com/yourusername/movie-recommender-system.git
cd movie-recommender-system
```

### Install dependencies

```
pip install -r requirements.txt
```

### Run the application

```
streamlit run app.py
```

---

## 📌 Future Improvements

- Add collaborative filtering
- Improve recommendation accuracy
- Enhance UI design
- Add movie search and filtering features

---

## 👨‍💻 Author

Avinash Raj  
B.Tech CSE | Full Stack Developer
