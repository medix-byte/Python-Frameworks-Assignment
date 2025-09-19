# src/app.py
import streamlit as st
from src.data_prep import load_metadata, basic_clean
import matplotlib.pyplot as plt

st.set_page_config(page_title="CORD-19 Explorer", layout="wide")
st.title("CORD-19 Data Explorer")
st.write("Simple exploration of COVID-19 research metadata")

@st.cache_data
def load_and_prepare(path="data/metadata_sample.csv"):
    df = load_metadata(path=path, nrows=None)
    df = basic_clean(df)
    return df

df = load_and_prepare()

if df['year'].dropna().empty:
    st.warning("No publish year data available.")
else:
    min_year = int(df['year'].dropna().min())
    max_year = int(df['year'].dropna().max())
    year_range = st.slider("Publication year range", min_year, max_year, (min_year, max_year))

    filtered = df[df['year'].between(year_range[0], year_range[1])]

    st.write(f"Displaying {len(filtered)} papers from {year_range[0]} to {year_range[1]}")

    st.subheader("Publications by Year")
    pub_counts = filtered['year'].value_counts().sort_index()
    fig1, ax1 = plt.subplots()
    pub_counts.plot(kind='bar', ax=ax1)
    ax1.set_xlabel("Year")
    ax1.set_ylabel("Count")
    st.pyplot(fig1)

    st.subheader("Top Journals")
    if 'journal' in filtered.columns:
        top_n = st.slider("Top N journals", 5, 30, 10)
        vc = filtered['journal'].fillna('Unknown').value_counts().head(top_n)
        st.bar_chart(vc)
    else:
        st.info("No journal column in dataset.")

    st.subheader("Sample records")
    show_cols = [c for c in ['title','authors','publish_time','journal'] if c in filtered.columns]
    st.dataframe(filtered[show_cols].head(50))
