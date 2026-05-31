import streamlit as st
import pickle
import requests
from config import API_KEY

# def recommend(movie):
#     movie_index = movies[movies['title'] == movie].index[0]
#     distances = similarity[movie_index]
#     movies_list = sorted(list(enumerate(distances),reverse=True,key = lambda x : x[1]))[1:6]
#     recommended_movies = []

#     for i in movies_list:
#         recommended_movies.append(movies.iloc[i[0]].title)
#     return recommended_movies
 
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"

    response = requests.get(url)

    data = response.json()

    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
        
    return recommended_movie_names, recommended_movie_posters


st.title("Movie Recommendation System")




movies = pickle.load(open('movie_list.pkl', 'rb'))
movie_list  =movies['title'].values
similarity = pickle.load(open('similarity.pkl', 'rb'))



st.markdown(
    """
    <style>
    /* Change cursor for selectbox */
    div[data-baseweb="select"] * {
        cursor: pointer !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
selected_movie_name = st.selectbox("Select a movie:", movie_list)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])
    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])