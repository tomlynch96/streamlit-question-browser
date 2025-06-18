import streamlit as st

st.title("My First Streamlit App 🎉")

st.header("Welcome to your cloud-based teaching tool")
st.write("This app will eventually let you browse and filter your AI-generated physics question bank.")

# Example interactive element
name = st.text_input("Enter your name")
if name:
    st.success(f"Hello, {name}! 👋")
