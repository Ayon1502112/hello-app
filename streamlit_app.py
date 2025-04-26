import streamlit as st

st.title("নিচের button গুলো click করে, app গুলো open করা যাবে")

# Define buttons with their URLs
urls = {
    "Die Maintenance data submit": "https://www.appsheet.com/start/d08c2dec-9273-48fa-a169-e71ee9e5eec3",
    "Priority List Wirecut Work": "https://www.appsheet.com/start/f6b450ff-9d67-405e-8dd7-fe906b8a9d3b",
    "Wirecut Data Submit": "https://www.appsheet.com/start/f2025d66-1faa-4eaf-8db1-f2001d08104c",
    "Dashboard (Wirecut Monitoring)": "https://lookerstudio.google.com/reporting/7ed9000d-a119-4655-9c6d-d311a1d23a28",
    "Die Backup Entry": "https://www.appsheet.com/start/a60117bc-5aaf-4595-aa19-3d7fd1c54e87",
    "Die Damage Incident Entry": "https://www.appsheet.com/start/dfd99944-3ba3-4fc6-8509-35a72a681e54",
    "Live Die Maintenance Report": "https://lookerstudio.google.com/reporting/6d689733-0d3c-4667-ac7f-ee96cd4f0523",
    "Job List Die Modification/Service": "https://www.appsheet.com/start/55d59741-2ae3-41a7-8d18-cc47a5775272"   
}

# Create buttons using st.link_button()
for name, url in urls.items():
    st.link_button(name, url)
