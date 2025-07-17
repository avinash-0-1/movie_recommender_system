import pickle
import streamlit as st
import requests
import os
import gdown
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")

# -- Google Drive download helper --
def download_model(file_id, output_path):
    if not os.path.exists(output_path):
        url = f'https://drive.google.com/uc?id={file_id}'
        gdown.download(url, output_path, quiet=False)

# -- Download the model files from Google Drive --
os.makedirs("model", exist_ok=True)
download_model('13YwYW5Zzqa1CloduU8v_AJTD3bJyaclO', 'model/movie_list.pkl')
download_model('1JKhqN_-rtqPDwY4kJP-XPOjxwgOzwJc6', 'model/similarity.pkl')

def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        poster_path = data.get('poster_path')
        if not poster_path:
            return "https://via.placeholder.com/300x450?text=No+Image"
        return "https://image.tmdb.org/t/p/w500/" + poster_path
    except Exception as e:
        print(f"[ERROR] Failed to fetch poster for movie ID {movie_id}: {e}")
        return "https://via.placeholder.com/300x450?text=No+Image"

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
    return recommended_movie_names, recommended_movie_posters

st.header('Movie Recommender System')

# ---------Load models------
movies = pickle.load(open('model/movie_list.pkl', 'rb'))
similarity = pickle.load(open('model/similarity.pkl', 'rb'))

# ---- custom CSS------
if os.path.exists("style.css"):
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

movie_list = movies['title'].values
selected_movie = st.selectbox("Type or select a movie from the dropdown", movie_list)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.text(recommended_movie_names[i])
            st.image(recommended_movie_posters[i])
