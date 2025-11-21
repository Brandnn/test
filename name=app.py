import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.set_page_config(page_title="Simple Deploy Demo", layout="centered")

st.title("Streamlit Deploy Demo")
st.write("This is a minimal Streamlit app you can deploy to share.streamlit.io.")

with st.sidebar:
    st.header("Controls")
    rows = st.slider("Number of rows", min_value=10, max_value=1000, value=100, step=10)
    seed = st.number_input("Random seed", min_value=0, value=42, step=1)
    show_table = st.checkbox("Show data table", value=True)

# Create demo dataframe
np.random.seed(seed)
df = pd.DataFrame({
    "x": np.arange(rows),
    "y": np.cumsum(np.random.randn(rows))
})

st.subheader("Line chart")
chart = alt.Chart(df).mark_line().encode(
    x="x",
    y="y"
).properties(width=700, height=400)
st.altair_chart(chart, use_container_width=True)

if show_table:
    st.subheader("Data")
    st.dataframe(df)

st.markdown("---")
st.info("To deploy: push this repo to GitHub, then on https://share.streamlit.io create a new app and point it to this repo and app.py (branch: main).")
