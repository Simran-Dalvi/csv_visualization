import streamlit as st
import pandas as pd

st.set_page_config(page_title="LLM Data Dashboard", layout="wide")

st.title("LLM Powerd DATA Dashboard for TITANIC dataset", text_alignment="center")

st.markdown("Ask your question about the data and get visual insights")

## Loading the dataset
@st.cache_data
def load_data():
    return pd.read_csv("data\\titanic.csv")

df = load_data()

st.subheader("DataSet Preview")
st.dataframe(df.head(10))

st.subheader("Ask your question")
user_prompt = st.text_input(
    "Example: Show survival rate by gender"
)