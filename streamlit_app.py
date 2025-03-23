import streamlit as st
import webbrowser

st.title("Open URLs with Buttons")

# Define buttons and their corresponding URLs
urls = {
    "Google": "https://www.google.com",
    "YouTube": "https://www.youtube.com",
    "GitHub": "https://www.github.com",
    "Stack Overflow": "https://stackoverflow.com"
}

for name, url in urls.items():
    if st.button(name):
        webbrowser.open_new_tab(url)  # Open in a new tab

