# 🛒 Amazon Reviews Analysis

> End-to-end NLP pipeline on Amazon Alexa product reviews

[![Open Notebook](https://img.shields.io/badge/Jupyter-Open_Notebook-F37626?logo=jupyter&logoColor=white)](https://github.com/evgeniimatveev/Python-Projects/blob/🛒-amazon-reviews-analysis/amazon_reviews_analysis.ipynb)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)](https://python.org)

## What you get

- Rating distribution and sentiment split (pie chart)
- Reviews over time (monthly trend)
- WordCloud — positive vs negative reviews
- Top 15 most frequent positive & negative words
- **TF-IDF + Logistic Regression** classifier with confusion matrix
- **BERT sentiment** (`nlptown/bert-base-multilingual-uncased-sentiment`) on sample reviews

## Tech Stack

| Tool | Purpose |
|------|---------|
| `pandas / numpy` | Data manipulation |
| `seaborn / matplotlib` | Visualisation |
| `wordcloud` | Word cloud generation |
| `scikit-learn` | TF-IDF vectoriser + Logistic Regression |
| `transformers` | BERT-based deep sentiment |

## Dataset

`amazon_alexa.tsv` — not included (download from [Kaggle](https://www.kaggle.com/datasets/sid321axn/amazon-alexa-reviews)).

## Quick Start

```bash
git checkout 🛒-amazon-reviews-analysis
pip install transformers wordcloud scikit-learn seaborn pandas
jupyter notebook amazon_reviews_analysis.ipynb
```

---

← [All Projects](https://github.com/evgeniimatveev/Python-Projects)