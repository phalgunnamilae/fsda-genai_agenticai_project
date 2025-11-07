import os
from langchain.chat_models import init_chat_model
import streamlit as st

os.environ["GOOGLE_API_KEY"] = "AIzaSyCmsmNqErhSOBBBX4w9E1cJ-QEA2kDGTxc"

model = init_chat_model("google_genai:gemini-2.5-flash-lite")

text_to_be_translated = st.text_area("Enter the text to be translated")

from langchain.messages import HumanMessage, AIMessage, SystemMessage

#Dictionary format

conversation = [
    {"role": "system", "content": "You are a helpful assistant that translates English to Telugu."},
    {"role": "user", "content": "Translate:" + text_to_be_translated}
]

response = model.invoke(conversation)

st.subheader("response")
st.success(response.content.strip())