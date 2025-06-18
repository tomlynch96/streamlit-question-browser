import streamlit as st

st.title("My First Streamlit App 🎉")

st.header("Welcome to your cloud-based teaching tool")
st.write("This app will eventually let you browse and filter your AI-generated physics question bank.")

# Example interactive element
name = st.text_input("Enter your name")
if name:
    st.success(f"Hello, {name}! 👋")

st.markdown("**Q:** What is the acceleration due to gravity on Earth?")
options = ["8.9 m/s²", "9.8 m/s²", "10.5 m/s²"]
choice = st.radio("Choose an answer:", options)

if choice:
    if choice == "9.8 m/s²":
        st.success("Correct! 🎉")
    else:
        st.error("Not quite. Try again.")
