
import streamlit as st 
import pandas as pd
import pickle as pk

# Define a function to recommend movies based on input movie
def recommend(movie):
    # Find the index of the input movie in the movie DataFrame
    movie_index = movie_df[movie_df['title']==movie].index[0]
    
    # Get the similarity scores for the input movie
    distance = similarity[movie_index]
    
    # Get the indexes of the top five most similar movies
    movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    
    # Get the titles of the recommended movies
    recommended_movies=[]
    #movie_id=i[0]
    #fatch  the poster from API
    for i in movies_list:
        recommended_movies.append(movie_df.iloc[i[0]].title)
    
    return recommended_movies

# Load the movie data
movies_dict = pk.load(open('movie.pkl', 'rb'))
movie_df = pd.DataFrame(movies_dict)

# Create a select box for choosing a movie
st.title("Movie Recommendation System")
selected_movie = st.selectbox("Select a movie", movie_df['title'].values)

# Load the pickled similarity matrix
similarity = pk.load(open('similarity.pkl', 'rb'))

# Create a button for generating recommendations
if st.button("Recommend"):
    # Call the recommend() function to get a list of recommended movies
    recommendations = recommend(selected_movie)
    
    # Display the recommended movies
    st.write("Recommended movies:")
    for movie in recommendations:
        st.write("- " + movie)