import streamlit as st
import pickle
import pandas as pd
import requests
#from streamlit import request
def fetch_poster(movies_id):
  response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=da54c5ca169a820853b8c6fbc1ebc3fc&language=en-US'.format(movies_id))
  data=response.json()
  return "https://image.tmdb.org/t/p/w500/" +data['poster_path']
def recommend(movie):
    movie_index = movies_list[movies_list['title'] == movie].index[0]
    distances = simillarity[movie_index]
    movies_list2 = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_posters=[]
    for i in movies_list2:
        movie_id = movies_list.iloc[i[0]].movie_id

        recommended_movies.append(movies_list.iloc[i[0]].title)
        # fetch poster from api
        recommended_movies_posters.append(fetch_poster(movie_id))
    return  recommended_movies,recommended_movies_posters

movies_list = pickle.load(open('movies.pkl','rb'))
simillarity = pickle.load(open('simillarity.pkl','rb'))
movies_list1=movies_list['title'].values
st.title('movie recommendation system')


selected_movies_name = st.selectbox('ENTER MOVIE FOR WHICH YOU WANT DIFFERENT MOVIE  RECOMMENDATION ?',
                      (movies_list1))
if st.button('recommend'):
    names,posters= recommend(selected_movies_name)

    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text (names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])

