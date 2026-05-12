# 📰 News Sentiment Analysis

A machine learning and NLP project that analyzes financial news headlines to determine sentiment (positive, negative, or neutral). The project includes exploratory data analysis (EDA), text preprocessing, feature engineering, model building, and unit testing.

---

## 📌 Project Overview

This project focuses on:

* Cleaning and preprocessing financial news text
* Performing exploratory data analysis (EDA)
* Visualizing sentiment patterns and most frequent words
* Extracting features using NLP techniques (TF-IDF, n-grams)
* Building and evaluating sentiment classification models
* Ensuring code quality using unit tests (pytest)

---

## 📂 Repository Structure

```
news-sentiment-analysis/
│
├── data/                  # Dataset files
├── notebooks/             # Jupyter notebooks
│   ├── task1_eda.ipynb
│   ├── task2_AAPL_eda.ipynb
│   ├── task2_AMZN_eda.ipynb
│   ├── task2_GOOG_eda.ipynb
|   ├── task2_META_eda.ipynb
│   ├── task2_NVDA_eda.ipynb
│   ├── task3_AAPL_fin.ipynb
│   ├── task3_AMZN_fin.ipynb
│   ├── task3_GOOG_fin.ipynb
|   ├── task3_META_fin.ipynb
│   ├── task3_NVDA_fin.ipynb
|
├── src/                   # Source code
│   ├── preprocessing.py   # Text cleaning functions
│   ├── features.py        # Feature engineering
│
├── tests/                 # Unit tests
│   ├── test_preprocessing.py
│
├── requirements.txt       # Dependencies
├── README.md              # Project documentation
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/fevenabebe/News-sentimental-analy.git
cd News-sentimental-analysis
```

### 2. Create virtual environment (recommended)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 How to Run the Project

### Run Jupyter Notebooks

```bash
jupyter notebook
```

Open:

* `notebooks/task1_eda.ipynb`
* `notebooks/task2_AAPL.ipynb`
* `notebooks/task2_AMZN_eda.ipynb
* `notebooks/task2_META_eda.ipynb
* `notebooks/task2_GOOG_eda.ipynb
* `notebooks/task2_NVDA_eda.ipynb
* `notebooks/task3_AAPL.ipynb`
* `notebooks/task3_AMZN_eda.ipynb
* `notebooks/task3_META_eda.ipynb
* `notebooks/task2_GOOG_eda.ipynb
* `notebooks/task3_NVDA_eda.ipynb


---

## 🧪 Running Tests

Unit tests ensure preprocessing functions work correctly.

### Run tests using pytest:

```bash
python -m pytest
```

Expected output:

```
2 passed
```

---

## 📊 Key Features

### 🔹 Exploratory Data Analysis (EDA)

* Sentiment distribution analysis
* Word frequency visualization
* Word cloud generation

### 🔹 NLP Preprocessing

* Lowercasing text
* Removing special characters and numbers
* Tokenization and cleaning

### 🔹 Feature Engineering

* TF-IDF vectorization
* Bigram analysis

### 🔹 Model Building

* Machine learning models for sentiment classification
* Evaluation using accuracy and other metrics

---

## 🧪 Example: Text Cleaning Function

```python
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-z\\s]', '', text)
    return text
```

---

## 📈 Results (Example)

* Most frequent sentiment: Neutral / Positive (depends on dataset)
* Key features: financial terms, company names, market words

---

## 🛠️ Technologies Used

* Python
* Pandas, NumPy
* Scikit-learn
* Matplotlib
* WordCloud
* Pytest
* Jupyter Notebook

---

## 👨‍💻 Author

Feven Abebe

---

## 📌 Notes

This project was built for academic evaluation and demonstrates:

* NLP preprocessing pipelines
* Exploratory data analysis
* Machine learning workflow
* Software engineering practices (modular code + testing)

---
