# 🎬 Similar Movie Recommender

This is a machine learning project that recommends similar movies based on user input.  
It uses a content-based filtering model and is powered by a **Streamlit frontend** for a smooth and interactive experience.  
The core logic is implemented in a **Jupyter Notebook**, and all required dependencies are included in `requirements.txt`.

---

## 🔍 Features

- 🔎 Get similar movie recommendations instantly
- 🎥 Clean and minimal **Streamlit-based UI**
- ⚙️ Content-based recommendation using machine learning
- 📁 Jupyter Notebook for model training and explanation
- ✅ All libraries listed in `requirements.txt`

---

## 🛠️ Tech Stack

- **Python**
- **Scikit-learn**
- **Pandas**
- **Numpy**
- **Streamlit**
- **Jupyter Notebook**

---

## 🧠 How It Works

- A content-based similarity matrix is created using TF-IDF or cosine similarity.
- When a user inputs a movie title, the system recommends the most similar movies based on plot/genre vectors.

---

## 🚀 Getting Started

1. **Clone the repository:**

    ```bash
   git clone https://github.com/vanshika-wadhwa/movie_Recommender.git
   cd movie_Recommender

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt

3. **Run the Streamlit app:**
    ```bash
    streamlit run app.py
## 📦 Git Large File Storage (LFS)

This project uses [Git LFS](https://git-lfs.github.com/) to store large model files (`.pkl`).

If you're cloning this repository, make sure Git LFS is installed on your system:

```bash
git lfs install
git lfs pull
