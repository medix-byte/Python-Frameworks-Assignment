# src/data_prep.py
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

def load_metadata(path="data/metadata.csv", nrows=None):
    """Load metadata.csv (use nrows for a sample)."""
    df = pd.read_csv(path, nrows=nrows)
    return df

def basic_clean(df):
    """Parse publish_time, extract year, ensure title/abstract exist, add abstract word count."""
    # try common date columns
    if 'publish_time' not in df.columns:
        for c in ['publish_time', 'publish_year', 'date', 'publication_date']:
            if c in df.columns:
                df['publish_time'] = pd.to_datetime(df[c], errors='coerce')
                break
    else:
        df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')

    df['year'] = df['publish_time'].dt.year
    df['title'] = df.get('title', '').fillna('').astype(str)
    df['abstract'] = df.get('abstract', '').fillna('').astype(str)
    df['abstract_wc'] = df['abstract'].apply(lambda x: len(x.split()))
    return df
