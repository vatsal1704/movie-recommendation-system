# import streamlit as st
# import pandas as pd
# import requests
# import pickle

# # Load the processed data and similarity matrix
# with open('movie_data.pkl', 'rb') as file:
#     movies, cosine_sim = pickle.load(file)

# # Function to get movie recommendations
# def get_recommendations(title, cosine_sim=cosine_sim):
#     idx = movies[movies['title'] == title].index[0]
#     sim_scores = list(enumerate(cosine_sim[idx]))
#     sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
#     sim_scores = sim_scores[1:11]  # Get top 10 similar movies
#     movie_indices = [i[0] for i in sim_scores]
#     return movies[['title', 'movie_id']].iloc[movie_indices]

# # Fetch movie poster from TMDB API
# def fetch_poster(movie_id):
#     api_key = '7b995d3c6fd91a2284b4ad8cb390c7b8'  # Replace with your TMDB API key
#     url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}'
#     response = requests.get(url)
#     data = response.json()
#     poster_path = data['poster_path']
#     full_path = f"https://image.tmdb.org/t/p/w500{poster_path}"
#     return full_path

# # Streamlit UI
# st.title("Movie Recommendation System")

# selected_movie = st.selectbox("Select a movie:", movies['title'].values)

# if st.button('Recommend'):
#     recommendations = get_recommendations(selected_movie)
#     st.write("Top 10 recommended movies:")

#     # Create a 2x5 grid layout
#     for i in range(0, 10, 5):  # Loop over rows (2 rows, 5 movies each)
#         cols = st.columns(5)  # Create 5 columns for each row
#         for col, j in zip(cols, range(i, i+5)):
#             if j < len(recommendations):
#                 movie_title = recommendations.iloc[j]['title']
#                 movie_id = recommendations.iloc[j]['movie_id']
#                 poster_url = fetch_poster(movie_id)
#                 with col:
#                     st.image(poster_url, width=130)
#                     st.write(movie_title)






# import streamlit as st
# import pandas as pd
# import requests
# import pickle
# from streamlit_option_menu import option_menu

# # Set page config
# st.set_page_config(
#     page_title="Movie Recommendation System",
#     page_icon="🎬",
#     layout="wide"
# )

# # Load data
# @st.cache_data
# def load_data():
#     with open('movie_dict.pkl', 'rb') as file:
#         movies_dict = pickle.load(file)
#     movies = pd.DataFrame(movies_dict)
#     similarity = pickle.load(open('similarity.pkl', 'rb'))
#     return movies, similarity

# movies, similarity = load_data()

# # Recommendation function
# def recommend(movie_title):
#     try:
#         idx = movies[movies['title'] == movie_title].index[0]
#         sim_scores = list(enumerate(similarity[idx]))
#         sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
#         sim_scores = sim_scores[1:11]  # Top 10 similar movies
#         movie_indices = [i[0] for i in sim_scores]
#         return movies['title'].iloc[movie_indices], movies['movie_id'].iloc[movie_indices]
#     except IndexError:
#         st.error("Movie not found in database. Please select another movie.")
#         return [], []

# # Fetch movie poster
# def fetch_poster(movie_id):
#     try:
#         api_key = st.secrets.get("TMDB_API_KEY", "7b995d3c6fd91a2284b4ad8cb390c7b8")  # Fallback to default key
#         url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}'
#         response = requests.get(url)
#         response.raise_for_status()
#         data = response.json()
#         poster_path = data.get('poster_path')
#         if poster_path:
#             return f"https://image.tmdb.org/t/p/w500{poster_path}"
#         return "https://via.placeholder.com/500x750?text=Poster+Not+Available"
#     except Exception as e:
#         st.error(f"Error fetching poster: {e}")
#         return "https://via.placeholder.com/500x750?text=Error+Loading+Poster"

# # Sidebar navigation
# with st.sidebar:
#     selected = option_menu(
#         "Main Menu",
#         ["Recommend Movies", "About"],
#         icons=["search", "info-circle"],
#         menu_icon="film",
#         default_index=0,
#     )

# # Main content
# if selected == "Recommend Movies":
#     st.title("🎬 Movie Recommendation System")
#     st.markdown("Discover movies similar to your favorites!")
    
#     col1, col2 = st.columns([3, 1])
#     with col1:
#         selected_movie = st.selectbox(
#             "Select a movie you like:",
#             movies['title'].values,
#             index=0,
#             help="Start typing to search for a movie"
#         )
    
#     if st.button('Get Recommendations', use_container_width=True):
#         with st.spinner('Finding similar movies...'):
#             recommended_titles, recommended_ids = recommend(selected_movie)
            
#             if recommended_titles.any():
#                 st.success(f"Movies similar to '{selected_movie}':")
                
#                 # Display in 2 rows of 5 columns each
#                 for i in range(0, 10, 5):
#                     cols = st.columns(5)
#                     for col, j in zip(cols, range(i, i+5)):
#                         if j < len(recommended_titles):
#                             with col:
#                                 st.image(
#                                     fetch_poster(recommended_ids.iloc[j]),
#                                     use_column_width=True,
#                                     caption=recommended_titles.iloc[j]
#                                 )

# elif selected == "About":
#     st.title("About This Project")
#     st.markdown("""
#     ### Movie Recommendation System
#     This system recommends movies based on content similarity using:
#     - **Content-Based Filtering**: Analyzes movie features to find similar items
#     - **TMDB API**: Fetches movie posters and additional details
    
#     **How it works:**
#     1. Select a movie you like
#     2. Click "Get Recommendations"
#     3. Discover similar movies
    
#     **Dataset:** Contains information about 5000+ movies
#     """)
    
#     st.markdown("---")
#     st.caption("Built with ❤️ using Python, Streamlit, and TMDB API")

# # Footer
# st.markdown("---")
# st.caption("Note: Movie data and posters are sourced from TMDB. This is for educational purposes only.")



























# import streamlit as st
# import pandas as pd
# import requests
# import pickle
# import gdown
# import os
# from streamlit_option_menu import option_menu

# # Set page config
# st.set_page_config(
#     page_title="Movie Recommendation System",
#     page_icon="🎬",
#     layout="wide"
# )

# # Load data using gdown (Google Drive)
# @st.cache_data
# def load_data():
#     file_id = "1WrdhTYpmcHa2m4zjDbdp0GKCM0m_hMmD"
#     url = f"https://drive.google.com/uc?id={file_id}"
#     output_path = "/tmp/movie_data.pkl"

#     if not os.path.exists(output_path):  # Avoid re-downloading on every run
#         gdown.download(url, output_path, quiet=False)

#     with open(output_path, "rb") as f:
#         movies, similarity = pickle.load(f)

#     return movies, similarity

# movies, similarity = load_data()

# # Recommendation function
# def recommend(movie_title):
#     try:
#         idx = movies[movies['title'] == movie_title].index[0]
#         sim_scores = list(enumerate(similarity[idx]))
#         sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
#         sim_scores = sim_scores[1:11]  # Top 10 similar movies
#         movie_indices = [i[0] for i in sim_scores]
#         return movies['title'].iloc[movie_indices], movies['movie_id'].iloc[movie_indices]
#     except IndexError:
#         st.error("Movie not found in database. Please select another movie.")
#         return [], []

# # Fetch movie poster
# def fetch_poster(movie_id):
#     try:
#         api_key = st.secrets.get("TMDB_API_KEY", "7b995d3c6fd91a2284b4ad8cb390c7b8")
#         url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}'
#         response = requests.get(url)
#         response.raise_for_status()
#         data = response.json()
#         poster_path = data.get('poster_path')
#         if poster_path:
#             return f"https://image.tmdb.org/t/p/w500{poster_path}"
#         return "https://via.placeholder.com/500x750?text=Poster+Not+Available"
#     except Exception as e:
#         st.error(f"Error fetching poster: {e}")
#         return "https://via.placeholder.com/500x750?text=Error+Loading+Poster"

# # Sidebar navigation
# with st.sidebar:
#     selected = option_menu(
#         "Main Menu",
#         ["Recommend Movies", "About"],
#         icons=["search", "info-circle"],
#         menu_icon="film",
#         default_index=0,
#     )

# # Main content
# if selected == "Recommend Movies":
#     st.title("🎬 Movie Recommendation System")
#     st.markdown("Discover movies similar to your favorites!")

#     col1, col2 = st.columns([3, 1])
#     with col1:
#         selected_movie = st.selectbox(
#             "Select a movie you like:",
#             movies['title'].values,
#             index=0,
#             help="Start typing to search for a movie"
#         )

#     if st.button('Get Recommendations', use_container_width=True):
#         with st.spinner('Finding similar movies...'):
#             recommended_titles, recommended_ids = recommend(selected_movie)

#             if recommended_titles.any():
#                 st.success(f"Movies similar to '{selected_movie}':")

#                 for i in range(0, 10, 5):
#                     cols = st.columns(5)
#                     for col, j in zip(cols, range(i, i + 5)):
#                         if j < len(recommended_titles):
#                             with col:
#                                 st.image(
#                                     fetch_poster(recommended_ids.iloc[j]),
#                                     use_column_width=True,
#                                     caption=recommended_titles.iloc[j]
#                                 )

# elif selected == "About":
#     st.title("About This Project")
#     st.markdown("""
#     ### Movie Recommendation System
#     This system recommends movies based on content similarity using:
#     - **Content-Based Filtering**
#     - **TMDB API** for movie posters
    
#     **Steps:**
#     1. Choose a movie
#     2. Click "Get Recommendations"
#     3. Enjoy suggestions!
#     """)

#     st.markdown("---")
#     st.caption("Built with ❤️ using Python, Streamlit, and TMDB API")

# # Footer
# st.markdown("---")
# st.caption("Note: Movie data and posters are sourced from TMDB. For educational use only.")







import streamlit as st
import pandas as pd
import requests
import pickle
import gdown
import os
from streamlit_option_menu import option_menu

# Page config
st.set_page_config(
    page_title="Movie Recommender 🎬",
    page_icon="🎥",
    layout="wide",
)

# Apply custom CSS for better UX
st.markdown("""
    <style>
        .stApp {
            background-color: #0e1117;
            color: white;
        }
        .movie-poster {
            border-radius: 12px;
            transition: transform 0.2s;
            box-shadow: 0 4px 8px rgba(0,0,0,0.3);
        }
        .movie-poster:hover {
            transform: scale(1.05);
        }
        .movie-title {
            text-align: center;
            font-weight: 500;
            margin-top: 8px;
        }
        .stButton > button {
            width: 100%;
            border-radius: 8px;
            font-weight: bold;
        }
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

# Load data from Google Drive
@st.cache_data
def load_data():
    file_id = "1WrdhTYpmcHa2m4zjDbdp0GKCM0m_hMmD"
    url = f"https://drive.google.com/uc?id={file_id}"
    output_path = "/tmp/movie_data.pkl"
    if not os.path.exists(output_path):
        gdown.download(url, output_path, quiet=False)
    with open(output_path, "rb") as f:
        movies, similarity = pickle.load(f)
    return movies, similarity

movies, similarity = load_data()

# Recommend movies
def recommend(movie_title):
    try:
        idx = movies[movies['title'] == movie_title].index[0]
        sim_scores = list(enumerate(similarity[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:11]
        movie_indices = [i[0] for i in sim_scores]
        return movies['title'].iloc[movie_indices], movies['movie_id'].iloc[movie_indices]
    except IndexError:
        st.error("Movie not found. Try another.")
        return [], []

# Get movie poster from TMDB
def fetch_poster(movie_id):
    try:
        api_key = st.secrets.get("TMDB_API_KEY", "7b995d3c6fd91a2284b4ad8cb390c7b8")
        url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}'
        response = requests.get(url)
        data = response.json()
        poster_path = data.get('poster_path')
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500{poster_path}"
        return "https://via.placeholder.com/500x750?text=No+Poster"
    except:
        return "https://via.placeholder.com/500x750?text=Error"

# Sidebar menu
with st.sidebar:
    selected = option_menu(
        "Menu",
        ["🎯 Recommend", "ℹ️ About"],
        icons=["search", "info-circle"],
        default_index=0,
    )

# Recommend Movies Page
if selected == "🎯 Recommend":
    st.title("🎬 Movie Recommendation System")
    st.subheader("Find movies similar to your favorites")

    selected_movie = st.selectbox(
        "Choose a movie:",
        movies['title'].values,
        index=0,
        help="Start typing to search"
    )

    if st.button("Get Recommendations"):
        with st.spinner("Loading recommendations..."):
            recommended_titles, recommended_ids = recommend(selected_movie)

        if recommended_titles.any():
            st.markdown("### Similar Movies:")

            for i in range(0, 10, 5):
                cols = st.columns(5)
                for col, j in zip(cols, range(i, i + 5)):
                    if j < len(recommended_titles):
                        with col:
                            poster_url = fetch_poster(recommended_ids.iloc[j])
                            st.markdown(f"<img src='{poster_url}' class='movie-poster' width='100%'/>", unsafe_allow_html=True)
                            # Removed the movie title under poster

# About Page
elif selected == "ℹ️ About":
    st.title("About This App")
    st.markdown("""
    This movie recommender uses **Content-Based Filtering** and **TMDB API**.

    **How to use:**
    1. Select a movie
    2. Click "Get Recommendations"
    3. View similar movies with posters

    **Tech stack:** Python · Streamlit · Pandas · Scikit-learn · TMDB API

    **Note:** For educational purposes only. Data © TMDB.
    """)
