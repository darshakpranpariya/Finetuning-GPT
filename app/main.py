import streamlit as st
import time
from llama_index import GPTSimpleVectorIndex
import os



os.environ["OPENAI_API_KEY"] = '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'

def ask_bot(message):
    index = GPTSimpleVectorIndex.load_from_disk('../index.json')
    response = index.query(message, response_mode="compact")
    return response.response

# Set the title and page layout
st.set_page_config(page_title="Chat UI", page_icon=":speech_balloon:", layout="wide")

# Define custom CSS styles for the text_area widget
st.write("""
    <style>
        .st-dm {
            padding: 0;
        }
    </style>
""", unsafe_allow_html=True)

# Set the app header and subheader
st.title("Welcome to the Tech Savvy Bot")
st.subheader("Enter your message below to start chatting:")

# Set the sidebar options
with st.sidebar:
    st.markdown("**Instructions:**")
    st.markdown("1. Type your message in the input field below")
    st.markdown("2. Click the 'Send' button or press Enter")
    st.markdown("3. Wait for the bot's response")
    st.markdown("4. Keep chatting!")

    st.markdown("---")
    st.markdown("**About:**")
    st.markdown("This app is made using fine tuning large language model(GPT) based on oops data of four programming languages(C,C++,Java,C#)")

# Create the chat UI
message_input = st.text_input("Your message:", key="input")
enter_pressed = st.session_state.get("enter_pressed", False)
if st.button("Send") or enter_pressed:
    st.session_state.enter_pressed = False
    if message_input:
        # Show a loading spinner while waiting for the bot's response
        with st.spinner("Thinking..."):
            time.sleep(2)
            # Generate a response and display it
            response = ask_bot(message_input)
            st.text_area("Bot:", value=response, key="output", height=300)
