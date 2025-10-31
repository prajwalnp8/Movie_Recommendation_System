import streamlit as st
import pickle
import base64

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image:
        encoded_string = base64.b64encode(image.read())
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), 
                              url(data:image/{"jpg"};base64,{encoded_string.decode()});
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
            color: white;
        }}
        .css-1d391kg {{
            background: rgba(0,0,0,0.6);
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Call background setup
add_bg_from_local(r"C:\Users\Prajwal\Desktop\movie_recommender\background.jpg")

# ------------------ Custom Page Styling ------------------
st.markdown("""
    <style>
    /* Center the title and increase its size */
    .title {
        text-align: center;
        font-size: 60px;
        font-weight: 800;
        color: #FFFFFF;
        text-shadow: 2px 2px 8px #000000;
        margin-bottom: 20px;
    }

    /* Subtitle / dropdown label styling */
    .subtitle {
        text-align: left;
        font-size: 22px;
        color: #D3D3D3;
        margin-bottom: 15px;
    }

    /* Center dropdown box */
    div[data-baseweb="select"] > div {
        margin: 0 auto;
        width: 60%;
    }

    /* Center button and style it */
    div.stButton > button {
        display: block;
        margin: 0 auto;
        font-size: 20px;
        font-weight: 600;
        background-color: #FF4B4B;
        color: white;
        border-radius: 10px;
        padding: 8px 24px;
    }
    </style>
""", unsafe_allow_html=True)


movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.markdown('<h1 class="title">🎬 Movie Recommendation System</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Select a movie to get recommendations:</p>', unsafe_allow_html=True)
selected_movie = st.selectbox(
    "",
    movies['title'].values
)

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

if st.button('Recommend'):
    recommendations = recommend(selected_movie)
    for i in recommendations:
        st.write(i)