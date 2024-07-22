import streamlit as st

# Sample data: List of dictionaries containing freedom fighter names and image URLs
freedom_fighters = [
    {"name": "Mahatma Gandhi", "image": "https://via.placeholder.com/150"},
    {"name": "Bhagat Singh", "image": "https://via.placeholder.com/150"},
    {"name": "Rani Lakshmi Bai", "image": "https://via.placeholder.com/150"},
    {"name": "Subhas Chandra Bose", "image": "https://via.placeholder.com/150"},
    {"name": "Sardar Vallabhbhai Patel", "image": "https://via.placeholder.com/150"},
    {"name": "Jawaharlal Nehru", "image": "https://via.placeholder.com/150"},
    {"name": "Bal Gangadhar Tilak", "image": "https://via.placeholder.com/150"},
    {"name": "Chandra Shekhar Azad", "image": "https://via.placeholder.com/150"}
]

def display_freedom_fighter(fighter, key):
    st.image(fighter["image"], width=150)
    st.text(fighter["name"])
    if st.button(f"Chat with {fighter['name']}", key=key):
        st.session_state.selected_fighter = fighter['name']
        st.switch_page("pages/Chat.py")

st.title("Freedom Fighters")

# Search bar
search_query = st.text_input("Search for a freedom fighter")

# Filter freedom fighters based on search query
filtered_fighters = [fighter for fighter in freedom_fighters if search_query.lower() in fighter['name'].lower()]

# Display freedom fighters in rows of four
num_columns = 4
for i in range(0, len(filtered_fighters), num_columns):
    cols = st.columns(num_columns)
    for j, col in enumerate(cols):
        if i + j < len(filtered_fighters):
            with col:
                display_freedom_fighter(filtered_fighters[i + j], f"button_{i+j}")
