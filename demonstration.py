import streamlit as st
import pandas as pd
import altair as alt


def show_image():
    with col2:
        st.image('https://i.imgur.com/8kIWGvb.png')


st.header("A simple demonstration of Streamlit")
st.subheader(f"We are currently using version {st.__version__}")

st.write("Hi! I'm a Streamlit app!")

col1, col2 = st.columns(2)

with col1:
    st.button("Click me!",
            help="This is a button. Click it to see what happens.",
            key="button1",
            on_click=show_image)

st.sidebar.write("We can put stuff in the sidebar too!")

st.sidebar.file_uploader(
    "Upload a file",
    help="This is an upload button.")
