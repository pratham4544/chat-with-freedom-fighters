import streamlit as st

st.title("About Me")

st.write("""
Welcome to my project! I'm Prathamesh Shete, the creator and developer of this platform. My goal is to make history engaging and interactive by allowing you to chat with virtual representations of Indian freedom fighters.
""")

# Centered profile card using columns and a styled container
st.markdown("<br>", unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown(
        """
        <div style="background-color: #f0f2f6; padding: 30px 20px; border-radius: 15px; box-shadow: 0 2px 8px rgba(0,0,0,0.07); text-align: center;">
            <img src="https://raw.githubusercontent.com/prathameshshete609/portfolio/main/assets/paddy.jpeg" alt="Profile" style="width: 140px; border-radius: 50%; margin-bottom: 15px;">
            <h2 style="margin-bottom: 5px;">Prathamesh Shete</h2>
            <p style="font-size: 1.1em; color: #555;"><b>Creator & Developer</b></p>
            <p>
                <a href="https://www.linkedin.com/in/prathameshshete/" target="_blank" style="text-decoration: none;">
                    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-original.svg" height="22" style="vertical-align:middle; margin-right:6px;">LinkedIn
                </a>
            </p>
            <p style="font-size: 1em; color: #333;">📧 prathameshshete609@gmail.com</p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("<br>", unsafe_allow_html=True)

if st.button("⬅️ Back to Home"):
    st.switch_page(page="Home.py")
