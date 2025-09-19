# src/analysis.py
from src.data_prep import load_metadata, basic_clean
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import re

sns.set(style="whitegrid")

def plot_publications_by_year(df, save_path=None):
    years = df['year'].dropna().astype(int)
    counts = years.value_counts().sort_index()
    fig, ax = plt.subplots(figsize=(8,4))
    counts.plot(kind='bar', ax=ax)
    ax.set_xlabel("Year")
    ax.set_ylabel("Number of papers")
    ax.set_title("Publications by Year")
    plt.tight_layout()
    if save_path:
        fig.savefig(save_path)
    plt.show()

def top_journals(df, n=15):
    col = 'journal' if 'journal' in df.columns else None
    if not col:
        print("No journal column found.")
        return
    vc = df[col].fillna('Unknown').value_counts().head(n)
    fig, ax = plt.subplots(figsize=(8,6))
    vc.sort_values().plot(kind='barh', ax=ax)
    ax.set_title(f"Top {n} Journals")
    plt.tight_layout()
    plt.show()

def title_word_freq(df, n=30):
    titles = df['title'].dropna().astype(str).str.lower()
    words = []
    for t in titles:
        tokens = re.findall(r"\b[a-z']{2,}\b", t)
        words.extend(tokens)
    stopwords = set(["the","and","for","with","from","study","on","in","to","of","covid","sars","2019","19"])
    filtered = [w for w in words if w not in stopwords]
    most = Counter(filtered).most_common(n)
    print("Top words in titles:", most)
    return most

if __name__ == "__main__":
    # use sample file to avoid memory issues; change nrows=None to load all
    try:
        df = load_metadata(path="data/metadata_sample.csv", nrows=None)
    except FileNotFoundError:
        print("data/metadata_sample.csv not found. Create sample or put metadata.csv into data/")
        raise

    df = basic_clean(df)
    print("Rows loaded:", len(df))
    plot_publications_by_year(df)
    top_journals(df)
    title_word_freq(df, 25)
