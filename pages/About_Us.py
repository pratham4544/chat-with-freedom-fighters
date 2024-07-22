import streamlit as st

st.title("About Us")

st.write("""
We are dedicated to bringing history to life through our interactive platform. Our goal is to educate and inspire by providing a unique experience where users can chat with virtual representations of Indian freedom fighters.
""")

if st.button("Back to Home"):
    st.switch_page(page="Home.py")
