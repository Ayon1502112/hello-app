import streamlit as st

# Set page configuration with no title or icon, using a wide layout
st.set_page_config(page_title="", page_icon=None, layout="wide")

# Custom CSS for styling
st.markdown("""
<style>
    .stApp {
        background: #ADD8E6;  /* Light blue background */
        color: black;
        font-family: sans-serif;
        padding: 20px;
    }
    .main .block-container {
        background-color: white;
        border-radius: 10px;
        padding: 30px;
        margin: auto;
        max-width: 800px;  /* Increased width for better tab layout */
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
    }
    .stMarkdown p {
        text-align: center;
        font-size: 1.5em;
        color: #333;
        font-weight: bold;
        margin-bottom: 30px;
    }
    .stLinkButton button {
        width: 100%;
        padding: 15px;
        margin-bottom: 15px;
        border-radius: 5px;
        border: 1px solid #ccc;
        background-color: white;
        color: #333;
        font-size: 1.2em;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    .stLinkButton button:hover {
        background-color: #f0f0f0;
    }
    .stLinkButton:first-of-type button {
        background-color: #ffebee;  /* Distinct light red for first button */
        color: #ef5350;
    }
    .stLinkButton:first-of-type button:hover {
        background-color: #ffcdd2;
    }
    .stTabs [data-baseweb="tab"] {
        font-size: 1.2em;
        font-weight: bold;
        color: #333;
        padding: 10px 20px;
    }
    .stTabs [data-baseweb="tab"]:hover {
        background-color: #f0f0f0;
    }
</style>
""", unsafe_allow_html=True)

# Subtitle to guide users
st.markdown("<p>নিচের ট্যাবগুলোতে ক্লিক করে, অ্যাপগুলো ওপেন করুন</p>", unsafe_allow_html=True)

# Define buttons with their URLs, grouped by category
tabs_data = {
    "Data Submission": [
        ("Die Maintenance data submit", "https://www.appsheet.com/start/d08c2dec-9273-48fa-a169-e71ee9e5eec3"),
        ("Wirecut Data Submit", "https://www.appsheet.com/start/f2025d66-1faa-4eaf-8db1-f2001d08104c"),
        ("Die Backup Entry", "https://www.appsheet.com/start/a60117bc-5aaf-4595-aa19-3d7fd1c54e87"),
        ("Die Damage Incident Entry", "https://www.appsheet.com/start/dfd99944-3ba3-4fc6-8509-35a72a681e54"),
        ("Hasan Bhai (VMC Entry)", "https://www.appsheet.com/start/8c16d536-adb4-4cdd-a1bb-e4a66e6753b2"),
        ("Maintenance Monitoring (Entry Form)", "https://www.appsheet.com/start/a81e8891-6548-4994-80c5-d7ec4f7d8c29"),
        ("Job List Die Modification/Service", "https://www.appsheet.com/start/55d59741-2ae3-41a7-8d18-cc47a5775272"),
    ],
    "Dashboards": [
        ("Dashboard (Wirecut Monitoring)", "https://lookerstudio.google.com/reporting/7ed9000d-a119-4655-9c6d-d311a1d23a28"),
        ("Live Die Maintenance Report", "https://lookerstudio.google.com/reporting/6d689733-0d3c-4667-ac7f-ee96cd4f0523"),
        ("Hasan Bhai (VMC Cutter Dashboard)", "https://lookerstudio.google.com/reporting/6556c179-2249-4fcf-9a52-5d8fbff20e3c"),
        ("Dashboard for Urgent maintenance", "https://lookerstudio.google.com/reporting/2b600a29-9938-4810-96db-a60eb99574ec"),
        ("No. Die Test", "https://lookerstudio.google.com/reporting/602b17d7-4a56-4a4c-8335-6bf523813c5a"),
    ],
    "Alerts": [
        ("Priority List Wirecut Work", "https://www.appsheet.com/start/f6b450ff-9d67-405e-8dd7-fe906b8a9d3b"),
        ("Transport Alert", "https://www.appsheet.com/start/8c342b26-93c9-4180-b4ae-007bc2a72643"),
    ],
}

# Create tabs
tab_names = list(tabs_data.keys())
tabs = st.tabs(tab_names)

# Populate each tab with its respective buttons
for tab, tab_name in zip(tabs, tab_names):
    with tab:
        for name, url in tabs_data[tab_name]:
            st.link_button(name, url)
