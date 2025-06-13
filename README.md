# 🎬 Movie Recommendation System

A simple yet powerful **Movie Recommendation System** that suggests personalized movie recommendations based on user preferences using **Cosine Similarity**. Whether you're looking for a movie similar to your favorite or just exploring new titles, this system helps you find the best match.

---

## 🚀 Overview

The goal of this project is to build a recommendation engine that recommends movies similar to a given title based on content features. This system primarily uses **Cosine Similarity** to measure the closeness between movie feature vectors and generate relevant suggestions.

---

## 🧠 How It Works

The recommendation system uses a **content-based filtering** approach. Here's a high-level view of the process:

1. **Dataset Preparation**: Movie metadata such as genres, cast, keywords, and crew are consolidated.
2. **Feature Engineering**: The relevant fields are combined into a single text format for each movie.
3. **Vectorization**: The text is transformed into a matrix of token counts using `CountVectorizer`.
4. **Similarity Computation**: Cosine Similarity is calculated between these vectors to find similar movies.
5. **Recommendation**: Based on the similarity scores, the top N most similar movies are returned.

---

## 🧾 Dataset Details

The dataset used in this project was sourced from **CACL (Center for Applied Computer Learning)** and includes extensive metadata for thousands of movies.

- Fields include: `title`, `overview`, `genres`, `keywords`, `cast`, `crew`, and `id`.
- The **TMDB API** (The Movie Database) was used to enrich the dataset with:
  - High-quality movie **posters**
  - Additional metadata like popularity and vote count

> 📁 **[Click here](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)** to access the dataset. *(Insert actual link)*

## 🌐 Live Demo

You can try out the live version of the project online:

👉 **[Click here](https://movie-recommendatiion-system.streamlit.app/)** to visit the Movie Recommendation System.

---

## 🛠️ How to Use

### 🔧 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/movie-recommendation-system.git
   cd movie-recommendation-system
