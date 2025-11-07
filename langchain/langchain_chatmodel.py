import os
from langchain.chat_models import init_chat_model
import streamlit as st

st.set_page_config(page_title="AI Translator", page_icon="🌐", layout="centered")
st.title("AI Chat bot")
st.write("Enter your question here")

os.environ["GOOGLE_API_KEY"] = "AIzaSyCmsmNqErhSOBBBX4w9E1cJ-QEA2kDGTxc"

# user inputs 

input_text = st.text_area("Enter your text here")

model = init_chat_model("google_genai:gemini-2.5-flash-lite")

response = model.invoke(input_text)

st.subheader("response")
st.success(response.content.strip())