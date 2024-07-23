import streamlit as st

st.title("Contact Us")

st.write("Have questions or feedback about Chat with Gita? We're here to help!")

# Create two columns
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

# Column 2: Contact information for Prathamesh
with col2:
    st.subheader("Prathamesh Shete")
    st.image('assets/paddy.jpeg', width=300)  # Adjust width as needed
    st.markdown("""
        - **Role:** Developer and Technical Lead
        - [LinkedIn](https://www.linkedin.com/in/prathameshshete/)
        - Email: prathameshshete609@gmail.com
    """)
