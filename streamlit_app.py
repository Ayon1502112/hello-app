import streamlit as st

# Minimal page config with only essential parameters
st.set_page_config(layout="wide")

# Inline CSS instead of cached function (reduces function call overhead)
CSS = """
<style>
body { background: #ADD8E6; font-family: sans-serif; }
.block-container { background: white; border-radius: 10px; padding: 30px; max-width: 800px; margin: auto; box-shadow: 0 4px 8px rgba(0,0,0,0.2);}
h2 { text-align: center; font-size: 1.5em; color: #333; margin-bottom: 20px;}
a.button { display: block; width: 100%; padding: 12px; margin: 8px 0; border-radius: 5px; text-align: center; background: white; border: 1px solid #ccc; color: #333; font-size: 1.1em; text-decoration: none; transition: background 0.3s ease;}
a.button:hover { background: #f0f0f0; }
a.button.first { background: #ffebee; color: #ef5350; }
a.button.first:hover { background: #ffcdd2; }
</style>
"""

# Pre-render all HTML content
TABS_DATA = {
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
    "Dashboards": [
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
        ("Remaining Task Wirecut/VMC (Entry)", "https://www.appsheet.com/start/b7a6c980-9901-4fdd-b968-35aafdd6f689"),
    ],
}

# Initialize session state variables
if 'active_tab' not in st.session_state:
    st.session_state.active_tab = list(TABS_DATA.keys())[0]
    st.session_state.links_html = ""

# Single markdown call for all static content
st.markdown(f"{CSS}<h2>নিচের ট্যাবগুলোতে ক্লিক করে, অ্যাপগুলো ওপেন করুন</h2>", unsafe_allow_html=True)

# Get current tab selection
active_tab = st.selectbox("Choose category", TABS_DATA.keys(), key='tab_selector')

# Build links HTML when tab changes or on first load
if st.session_state.active_tab != active_tab or not st.session_state.links_html:
    st.session_state.active_tab = active_tab
    st.session_state.links_html = "".join(
        f'<a href="{url}" target="_blank" class="button{' first' if i==0 else ''}">{name}</a>'
        for i, (name, url) in enumerate(TABS_DATA[active_tab])
    )

# Display the links
st.markdown(st.session_state.links_html, unsafe_allow_html=True)
