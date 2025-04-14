import streamlit as st
import pickle
import pandas as pd
#api library
import requests

def fetch_poster(id):
    response= requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(id))
    data= response.json()
    # st.text(data)
    # st.text('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(id))
    return "https://image.tmdb.org/t/p/w500" + data['poster_path'] # poster image + poster path


def recommend(movie):
  movie_index = movies[movies['title']== movie].index[0]
  distances= similarity[movie_index]
  movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]

  # recommended_list=[] ==> storage for nearest movie
  recommended_list = []
  recommended_list_poster=[]
  for i in movies_list:
    #   fetching poster pictures through id =i[0] from api
    movie_id= movies.iloc[i[0]].id

    recommended_list.append(movies.iloc[i[0]].title)
    # appending poster id
    recommended_list_poster.append(fetch_poster(movie_id))
  return recommended_list, recommended_list_poster


# fetching
movies_dict= pickle.load(open('movies_dict.pkl', 'rb'))
movies=pd.DataFrame(movies_dict)
similarity=pickle.load(open('similarity.pkl', 'rb'))


st.title("Movie Recommender System")

selected_movie_name= st.selectbox(
    'Hello, How would you like to contacted?',
    movies['title'].values
)
if st.button('Recommend'):
    names, poster = recommend(selected_movie_name)
    #  for display ==> layout your app
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(poster[0])
    with col2:
        st.text(names[1])
        st.image(poster[1])
    with col3:
        st.text(names[2])
        st.image(poster[2])
    with col4:
        st.text(names[3])
        st.image(poster[3])
    with col5:
        st.text(names[4])
        st.image(poster[4])


