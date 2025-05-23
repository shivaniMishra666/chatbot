import os
from dotenv import load_dotenv
import streamlit as st
from groq import Groq

# Load environment variables
load_dotenv()

# Initialize Groq client with error handling
api_key = os.environ.get("GROQ_API_KEY")
if not api_key:
    st.error("GROQ_API_KEY not found. Please make sure it's set in your environment variables.")
    st.stop()

# Initialize Groq client
client = Groq(api_key=api_key)

# Streamlit UI setup
st.title("Groq Chat Interface")
st.write("Ask a question and get an answer from Llama 3.3 70B.")

# Input field for user question
prompt = st.text_input("Enter your question:", key="user_input")

# Submit button
if st.button("Submit"):
    if prompt:
        with st.spinner("Getting response..."):
            try:
                # Create chat completion
                chat_completion = client.chat.completions.create(
                    messages=[
                        {
                            "role": "user",
                            "content": prompt,
                        }
                    ],
                    model="llama-3.3-70b-versatile",
                )
                
                # Display the response
                st.markdown("### Response:")
                st.write(chat_completion.choices[0].message.content)
            except Exception as e:
                st.error(f"Error communicating with Groq API: {str(e)}")
    else:
        st.warning("Please enter a question first.")
