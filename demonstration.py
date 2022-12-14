import streamlit as st
import pandas as pd
import altair as alt


st.header("A simple demonstration of Streamlit")

st.info(f"We are currently using version {st.__version__}")

st.write("Hello from the JGI!")

st.button("Here is a button.")

st.sidebar.image("generic_logo.png")

st.sidebar.write("This is a sidebar")

my_line = st.sidebar.radio(
    "Select things",
    ["Buying power", "Dollar Value", "Inflation Rate"],
    help="We use this to select items.")

user_data = st.sidebar.file_uploader(
    "Upload a file",
    help="This is an upload button.")


if user_data is not None:

    user_dataframe = pd.read_csv(user_data)

    melted = pd.melt(user_dataframe, id_vars=["Year"])

    years = [
        1800, 1825, 1850, 1875,
        1900, 1925, 1950, 1975, 2000]

    chart = alt.Chart(melted).mark_line().encode(
        x=alt.X("Year:Q", axis=alt.Axis(values=years)),
        y=alt.Y("value:Q"),
        color="variable:N",
        tooltip=["Year", "value", "variable"],
    ).interactive()

    st.altair_chart(chart, use_container_width=True)