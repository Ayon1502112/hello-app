import streamlit as st

st.set_page_config(page_title="", page_icon=None, layout="wide")

# Minimal CSS – single injection
st.markdown("""
<style>
body {
    background: #ADD8E6;
    font-family: sans-serif;
}
.block-container {
    background-color: white;
    border-radius: 10px;
    padding: 30px;
    max-width: 800px;
    margin: auto;
    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
}
h2 {
    text-align: center;
    font-size: 1.5em;
    color: #333;
}
a.button {
    display: block;
    width: 100%;
    padding: 12px;
    margin: 8px 0;
    border-radius: 5px;
    text-align: center;
    background: white;
    border: 1px solid #ccc;
    color: #333;
    font-size: 1.1em;
    text-decoration: none;
    transition: background 0.3s ease;
}
a.button:hover { background: #f0f0f0; }
a.button.first { background: #ffebee; color: #ef5350; }
a.button.first:hover { background: #ffcdd2; }
</style>
""", unsafe_allow_html=True)

st.markdown("<h2>নিচের ট্যাবগুলোতে ক্লিক করে, অ্যাপগুলো ওপেন করুন</h2>", unsafe_allow_html=True)

tabs_data = {
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

tab_names = list(tabs_data.keys())
active_tab = st.selectbox("Choose category", tab_names)

# Render only selected tab's links
for i, (name, url) in enumerate(tabs_data[active_tab]):
    cls = "button first" if i == 0 else "button"
    st.markdown(f'<a href="{url}" target="_blank" class="{cls}">{name}</a>', unsafe_allow_html=True)
