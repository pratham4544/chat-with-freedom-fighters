import streamlit as st
import json

# Function to save forum data to a local file
def save_forum_data(forum_data, filename='forum_data.json'):
    with open(filename, 'w') as f:
        json.dump(forum_data, f)

# Function to load forum data from a local file
def load_forum_data(filename='forum_data.json'):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Load forum data
if 'forum_data' not in st.session_state:
    st.session_state.forum_data = load_forum_data()

st.title("Forum")

# Display existing questions and comments
for idx, item in enumerate(st.session_state.forum_data):
    question, comments, likes = item
    st.subheader(f"Q{idx + 1}: {question}")
    st.write(f"Likes: {likes}")
    
    if st.button(f"Like Q{idx + 1}", key=f"like_{idx}"):
        st.session_state.forum_data[idx][2] += 1
        save_forum_data(st.session_state.forum_data)
        st.experimental_rerun()
    
    for comment in comments:
        st.write(f"- {comment}")
    
    with st.expander("Add a comment"):
        new_comment = st.text_area(f"Comment on Q{idx + 1}", key=f"comment_{idx}")
        if st.button(f"Add Comment to Q{idx + 1}", key=f"add_comment_{idx}"):
            if new_comment:
                st.session_state.forum_data[idx][1].append(new_comment)
                save_forum_data(st.session_state.forum_data)
                st.experimental_rerun()

# Allow users to post new questions
with st.form(key='new_question_form'):
    new_question = st.text_input("Ask a question")
    submit_button = st.form_submit_button("Post Question")
    if submit_button:
        if new_question:
            st.session_state.forum_data.append([new_question, [], 0])
            save_forum_data(st.session_state.forum_data)
            st.experimental_rerun()

if st.button("Back to Home"):
    st.switch_page("Home.py")
