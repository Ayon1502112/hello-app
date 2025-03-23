import streamlit as st

st.title("Open URLs with Buttons")

# Define buttons with their URLs
urls = {
    "Google": "https://www.google.com",
    "YouTube": "https://www.youtube.com",
    "GitHub": "https://www.github.com",
    "Stack Overflow": "https://stackoverflow.com"
}

# Create buttons using st.link_button()
for name, url in urls.items():
    st.link_button(name, url)
