import streamlit as st

st.title("About Us")

st.write("""
We are dedicated to bringing history to life through our interactive platform. Our goal is to educate and inspire by providing a unique experience where users can chat with virtual representations of Indian freedom fighters.
""")
col1, col2 = st.columns([1, 1])

# Column 1: Contact information for Reenal
with col1:
    st.subheader("Reenal Boddul")
    st.image('assets/reenal.jpeg', width=300)  # Adjust width as needed
    st.markdown("""
        - **Role:** Idea, Project Thoughts And Tech Lead
        - [LinkedIn](https://www.linkedin.com/in/reenal-zampal-boddul)
        - Email: reenalboddul@gmail.com
    """)
    
with col2:    
    st.subheader("Prathamesh Shete")
    st.image('assets/paddy.jpeg', width=300)  # Adjust width as needed
    st.markdown("""
        - **Role:** Developer and Technical Lead
        - [LinkedIn](https://www.linkedin.com/in/prathameshshete/)
        - Email: prathameshshete609@gmail.com
""")

if st.button("Back to Home"):
    st.switch_page(page="Home.py")
