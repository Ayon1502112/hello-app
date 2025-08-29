import streamlit as st

# Configure page settings
st.set_page_config(
    page_title="",
    page_icon=None,
    layout="wide"
)

# Apply custom styling
st.markdown(
    """
    <style>
        .stApp {
            background: #ADD8E6;
            color: black;
            font-family: sans-serif;
            padding: 20px;
        }
        .main .block-container {
            background-color: white;
            border-radius: 10px;
            padding: 30px;
            margin: auto;
            max-width: 800px;
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
            background-color: #ffebee;
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
    """,
    unsafe_allow_html=True
)

# Display user guidance
st.markdown(
    "<p>নিচের ট্যাবগুলোতে ক্লিক করে, অ্যাপগুলো ওপেন করুন</p>",
    unsafe_allow_html=True
)

# Application data organized by categories
APPLICATION_DATA = {
    "Data Entry 01": [
        ("Daily Die Maintenance Entry", "https://www.appsheet.com/start/d08c2dec-9273-48fa-a169-e71ee9e5eec3"),
        ("Wirecut Data Entry", "https://www.appsheet.com/start/f2025d66-1faa-4eaf-8db1-f2001d08104c"),
        ("Die Backup/Wastage Entry", "https://www.appsheet.com/start/a60117bc-5aaf-4595-aa19-3d7fd1c54e87"),
        ("Die Accident Entry", "https://www.appsheet.com/start/dfd99944-3ba3-4fc6-8509-35a72a681e54"),
        ("Hasan Bhai (VMC Cutter Calculation)", "https://www.appsheet.com/start/8c16d536-adb4-4cdd-a1bb-e4a66e6753b2"),
        ("Urgent Maintenance (Entry Form)", "https://www.appsheet.com/start/a81e8891-6548-4994-80c5-d7ec4f7d8c29"),
        ("Priority List Wirecut Work", "https://www.appsheet.com/start/f6b450ff-9d67-405e-8dd7-fe906b8a9d3b"),
        ("Job List Die Modification/Service", "https://www.appsheet.com/start/55d59741-2ae3-41a7-8d18-cc47a5775272"),
    ],
    "Dashboards 01": [
        ("Dashboard (Wirecut Monitoring)", "https://lookerstudio.google.com/reporting/7ed9000d-a119-4655-9c6d-d311a1d23a28"),
        ("Total Die Maintenance Report", "https://lookerstudio.google.com/reporting/6d689733-0d3c-4667-ac7f-ee96cd4f0523"),
        ("Dashboard (VMC/Wirecut CAM Task Remained)", "https://lookerstudio.google.com/reporting/cc1b4b03-3301-432e-92d5-35cb6bbda73f"),
        ("Hasan Bhai (VMC Cutter Dashboard)", "https://lookerstudio.google.com/reporting/6556c179-2249-4fcf-9a52-5d8fbff20e3c"),
        ("Dashboard for Urgent maintenance", "https://lookerstudio.google.com/reporting/2b600a29-9938-4810-96db-a60eb99574ec"),
        ("Die Backup/Wastage/Accident Report", "https://lookerstudio.google.com/reporting/ef474d7a-626f-43b3-9d20-271603f677ea"),
        ("Search Die Info", "https://script.google.com/a/~/macros/s/AKfycbyoLxXB_UEUvNzufJZ6vkwc9X6ifK_XErKCHIYfxxF6WS6eCAxPFWfvbQAVwKFVQVqs/exec"),
    ],
    "Data Entry 02": [
        ("Modification (Entry)", "https://www.appsheet.com/start/7a765b66-b7d3-4e9d-b546-6002c91482d4"),
        ("Milling Machine (Entry)", "https://www.appsheet.com/start/39113ebf-d65e-47e7-a271-5e0ea8bc6e8f"),
        ("Die Team Leader (Entry)", "https://www.appsheet.com/start/92286a91-59e3-4a60-b9e4-5eec572e999d"),
        ("Remaining Task Wirecut/VMC (Entry)", "https://www.appsheet.com/start/b7a6c980-9901-4fdd-b968-35aafdd6f689"),
    ],
}

# Create interface tabs
category_tabs = st.tabs(list(APPLICATION_DATA.keys()))

# Populate each tab with its applications
for tab, category in zip(category_tabs, APPLICATION_DATA):
    with tab:
        for app_name, app_url in APPLICATION_DATA[category]:
            st.link_button(app_name, app_url)
