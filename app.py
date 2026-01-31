import streamlit as st
import pandas as pd
from llm_planner import generate_analysis_plan
from dashboard import create_chart
from dotenv import load_dotenv
import json

load_dotenv()


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



if user_prompt:
    with st.spinner("Thinking..."):
        try:
            plan = generate_analysis_plan(
                user_prompt=user_prompt,
                columns=list(df.columns)
            )
        except Exception as e:
            st.error(f"LLM planning failed: {e}")
            st.stop()

    st.subheader("LLM Analysis Plan")
    st.json(plan)

    try:
        fig = create_chart(df, plan)
        st.plotly_chart(fig, use_container_width=True)
    except Exception as e:
        st.error(f"Error generating chart: {e}")
