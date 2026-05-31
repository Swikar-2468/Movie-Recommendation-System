# 🎥 Movie Recommendation System

A content-based movie recommendation system built on the **TMDB 5000 Movie Dataset**. It uses NLP and cosine similarity to find movies with similar content profiles, and presents results through a Streamlit web app with live posters fetched from the TMDb API.

---

## 🧠 How It Works

This system is **content-based**, not collaborative. It recommends movies by analyzing *what* a movie is about, not what other users watched.

### ML Pipeline (notebook)

1. **Data Loading** — Two CSVs are merged: `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv`, joined on the movie title.
2. **Feature Extraction** — Five content signals are extracted and combined into a single `tags` field per movie:
   - Plot overview
   - Genres
   - Top 3 keywords
   - Top 3 cast members
   - Director (from crew)
3. **Text Preprocessing** — Tags are lowercased and stemmed using NLTK's `PorterStemmer` to normalize word forms (e.g., "fighting" → "fight").
4. **Vectorization** — `CountVectorizer` (top 5000 features, English stop words removed) converts the tags into a `(4806, 5000)` sparse matrix.
5. **Similarity Matrix** — Pairwise **cosine similarity** is computed across all 4806 movies, producing a `(4806, 4806)` matrix.
6. **Serialization** — The processed movie DataFrame and similarity matrix are saved as `movie_list.pkl` and `similarity.pkl` for use by the app.

### Recommendation Logic (app.py)

Given a selected movie, the app:
- Looks up its index in the DataFrame
- Sorts all other movies by cosine similarity (descending)
- Returns the top 5 matches (excluding the movie itself)
- Fetches each movie's poster from the **TMDb API**

---

## 🚀 Features

- Content-based filtering using NLP (no user history needed)
- Rich tag construction from genres, cast, crew, keywords, and overview
- PorterStemmer normalization for better text matching
- Live movie poster display via TMDb API
- Clean 5-column Streamlit grid layout

---

## 🛠️ Tech Stack

| Layer | Tools |
|---|---|
| Data Processing | pandas, numpy |
| NLP | NLTK (PorterStemmer), scikit-learn (CountVectorizer) |
| ML | scikit-learn (cosine_similarity) |
| Serialization | pickle |
| Frontend | Streamlit |
| Poster API | TMDb API v3 |

---

## 📦 Dataset

**TMDB 5000 Movie Dataset** (available on Kaggle)
- `tmdb_5000_movies.csv` — movie metadata (genres, keywords, overview, etc.)
- `tmdb_5000_credits.csv` — cast and crew data

The pipeline processes ~4806 movies after merging and cleaning.

---

## 📦 Installation

### Prerequisites
- Python 3.x
- A [TMDb API key](https://www.themoviedb.org/settings/api)

### Steps

```bash
git clone https://github.com/your-repo/movie-recommendation-system.git
cd movie-recommendation-system
pip install -r requirements.txt
```

> **Note:** Before running the app, run the Jupyter notebook  `movie_recommender_nb.ipynb` to generate `movie_list.pkl` and `similarity.pkl`. These are required by `app.py` and are not included in the repo due to file size.

```bash
streamlit run app.py
```

---

## 📂 Project Structure
```markdown
movie-recommendation-system/
├── app.py
├── requirements.txt
├── movie_list.pkl
├── similarity.pkl
└── README.md
```
## 📸 Screenshots
<img width="1912" height="1012" alt="Screenshot 2026-05-31 094245" src="https://github.com/user-attachments/assets/7fe27446-0a68-4bfb-97d6-cb597924d464" />


## 🤝 Contributing
Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request.

## 📝 License
This project is licensed under the MIT License.

## 📬 Contact
For any questions or concerns, please contact us at [swikarbasnet30@gmail.com](mailto:swikarbasnet30@gmail.com).

## 💖 Thanks Message
Thank you for using our movie recommendation system! We hope you find it helpful.
