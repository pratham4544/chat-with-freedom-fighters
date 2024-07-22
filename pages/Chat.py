import streamlit as st

# Ensure a character is selected before displaying the chat
if 'selected_fighter' not in st.session_state:
    st.warning("Please select a character from the home page.")
    st.stop()

st.header(f"Chat with {st.session_state.selected_fighter}")

if 'messages' not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    st.write(message)

# Input for new message
user_input = st.text_input("You: ", "")

if st.button("Send"):
    if user_input:
        st.session_state.messages.append(f"You: {user_input}")
        # Here you can add the logic for the character's response
        st.session_state.messages.append(f"{st.session_state.selected_fighter}: This is an automated response.")
        user_input = ""

if st.button("Back"):
    st.switch_page("Home.py")
