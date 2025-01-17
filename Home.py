import streamlit as st

st.set_page_config(
    page_title="Chat with Indian Freedom Fighters",
    page_icon="🇮🇳",  # Indian flag emoji as the icon
    layout="wide",  # Setting the layout to wide
    initial_sidebar_state="expanded", # Sidebar state set to expanded by default
)


# Title of the app
st.title("Chat with Indian Freedom Fighters")

st.image('assets/homepage.jpg',use_column_width=True)

# Description
st.write("""
Welcome to our app where you can learn about and chat with the brave Indian freedom fighters who played pivotal roles in India's struggle for independence. Explore the lives and contributions of these heroes.
""")

# Navigation buttons
if st.button("Check the List of Freedom Fighters"):
    st.switch_page("pages/Freedom_Fighters.py")

if st.button("About Us"):
    st.switch_page("pages/About_Us.py")
    
if st.button("Forum"):
    st.switch_page("pages/Forum.py")
