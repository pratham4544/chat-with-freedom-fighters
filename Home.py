import streamlit as st

st.set_page_config(
    page_title="Chat with Indian Freedom Fighters",
    page_icon="🇮🇳",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Hide Streamlit's default sidebar hamburger and footer for a cleaner look

# Title of the app
st.title("Chat with Indian Freedom Fighters")

st.image('assets/homepage.jpg', use_column_width=True)

# Description
st.write("""
Welcome to my project! Here you can learn about and chat with the brave Indian freedom fighters who played pivotal roles in India's struggle for independence. Explore the lives and contributions of these heroes.
""")

# Center navigation buttons using columns as spacers
st.markdown("<br>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    if st.button("Check the List of Freedom Fighters"):
        st.switch_page("pages/Freedom_Fighters.py")
with col2:
    if st.button("About Me"):
        st.switch_page("pages/About_Us.py")

