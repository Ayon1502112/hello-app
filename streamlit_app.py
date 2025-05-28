import streamlit as st

# Set page configuration for a wider layout and potentially a background color
st.set_page_config(layout="wide", page_title="অ্যাপ লক্ষ্যর", page_icon=":house_buildings:")

# Custom CSS for styling the UI to resemble the image
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(to bottom right, #8a2be2, #4169e1);
        color: black;
        font-family: sans-serif;
        padding: 20px;
    }
    .main .block-container {
        background-color: white;
        border-radius: 10px;
        padding: 30px;
        margin: auto;
        max-width: 600px; # Limit the width of the content area
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
    }
    h1 {
        text-align: center;
        color: #4b0082;
        font-size: 2.5em;
        margin-bottom: 10px;
    }
    .stMarkdown p {
        text-align: center;
        font-size: 1.1em;
        color: #555;
        margin-bottom: 30px;
    }
    .stLinkButton button {
        width: 100%;
        padding: 15px;
        margin-bottom: 15px;
        border-radius: 5px;
        border: none;
        background-color: #f0f0f0; /* Default button color */
        color: #333;
        font-size: 1.2em;
        cursor: pointer;
        transition: background-color 0.3s ease;
        display: flex;
        align-items: center;
        justify-content: flex-start;
        gap: 15px;
    }
    .stLinkButton button:hover {
        background-color: #e0e0e0;
    }

    /* Specific styling for the first button (warning color) */
    .stLinkButton:first-of-type button {
        background-color: #ffebee; /* Light red background */
        color: #ef5350; /* Red text color */
    }
    .stLinkButton:first-of-type button:hover {
         background-color: #ffcdd2;
    }

     /* Add icons based on button text - This requires finding appropriate Streamlit icons or using external SVGs/images */
     .stLinkButton button::before {
         content: ''; /* Empty content for the icon */
         display: inline-block;
         width: 24px; /* Icon size */
         height: 24px; /* Icon size */
         background-size: contain;
         background-repeat: no-repeat;
         background-position: center;
         margin-right: 10px;
         vertical-align: middle;
     }

     /* Define icons for specific buttons */
     .stLinkButton:contains('Die Maintenance data submit') button::before {
         content: '⚠️'; /* Warning icon */
     }
     .stLinkButton:contains('Priority List Wirecut Work') button::before {
         content: '📋'; /* Clipboard icon */
     }
      .stLinkButton:contains('Wirecut Data Submit') button::before {
         content: '➡️'; /* Right arrow icon */
     }
     .stLinkButton:contains('Dashboard (Wirecut Monitoring)') button::before {
         content: '📊'; /* Bar chart icon */
     }
     .stLinkButton:contains('Die Backup Entry') button::before {
         content: '☁️'; /* Cloud icon */
     }
     .stLinkButton:contains('Die Damage Incident Entry') button::before {
         content: '❗'; /* Exclamation icon */
     }
      .stLinkButton:contains('Live Die Maintenance Report') button::before {
         content: '📈'; /* Line chart icon */
     }
      .stLinkButton:contains('Hasan Bhai (VMC Entry)') button::before {
         content: '👤'; /* Person icon */
     }
      .stLinkButton:contains('Hasan Bhai (VMC Cutter Dashboard)') button::before {
         content: '⚙️'; /* Gear icon */
     }
      .stLinkButton:contains('Maintenance Monitoring (Entry Form)') button::before {
         content: '🛠️'; /* Hammer and wrench icon */
     }
     .stLinkButton:contains('Job List Die Modification/Service') button::before {
         content: '📝'; /* Memo icon */
     }
     .stLinkButton:contains('Service') button::before {
         content: '🔧'; /* Wrench icon */
     }


</style>
""", unsafe_allow_html=True)

# Header with the app icon (using a large character as a placeholder)
st.markdown('<div style="text-align:center; font-size: 3em; color: #4b0082;">■■<br>■■</div>', unsafe_allow_html=True)
st.markdown("<h1>অ্যাপ লক্ষ্যর</h1>", unsafe_allow_html=True)
st.markdown("<p>নিচের বোতামগুলোতে ক্লিক করে, অ্যাপগুলো ওপেন করা যাবে</p>", unsafe_allow_html=True)


# Define buttons with their URLs
urls = {
    "Die Maintenance data submit": "https://www.appsheet.com/start/d08c2dec-9273-48fa-a169-e71ee9e5eec3",
    "Priority List Wirecut Work": "https://www.appsheet.com/start/f6b450ff-9d67-405e-8dd7-fe906b8a9d3b",
    "Wirecut Data Submit": "https://www.appsheet.com/start/f2025d66-1faa-4eaf-8db1-f2001d08104c",
    "Dashboard (Wirecut Monitoring)": "https://lookerstudio.google.com/reporting/7ed9000d-a119-4655-9c6d-d311a1d23a28",
    "Die Backup Entry": "https://www.appsheet.com/start/a60117bc-5aaf-4595-aa19-3d7fd1c54e87",
    "Die Damage Incident Entry": "https://www.appsheet.com/start/dfd99944-3ba3-4fc6-8509-35a72a681e54",
    "Live Die Maintenance Report": "https://lookerstudio.google.com/reporting/6d689733-0d3c-4667-ac7f-ee96cd4f0523",
    "Hasan Bhai (VMC Entry)": "https://www.appsheet.com/start/8c16d536-adb4-4cdd-a1bb-e4a66e6753b2",
    "Hasan Bhai (VMC Cutter Dashboard)": "https://lookerstudio.google.com/reporting/6556c179-2249-4fcf-9a52-5d8fbff20e3c",
    "Maintenance Monitoring (Entry Form)": "https://www.appsheet.com/start/a81e8891-6548-4994-80c5-d7ec4f7d8c29",
    "Job List Die Modification/Service": "https://www.appsheet.com/start/55d59741-2ae3-41a7-8d18-cc47a5775272",
    "Service": "https://lookerstudio.google.com/reporting/2b600a29-9938-4810-96db-a60eb99574ec"
}

# Create buttons using st.link_button()
for name, url in urls.items():
    st.link_button(name, url)

# Footer text
st.markdown("<p style='text-align:center; font-size: 0.9em; color: #777; margin-top: 30px;'>একটি সুন্দর অ্যাপ অভিজ্ঞতার জন্য ডিজাইন করা হয়েছে।</p>", unsafe_allow_html=True)
