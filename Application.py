import streamlit as st
st.title("welcome to my app")

import google.generativeai as genai

genai.configure(api_key="AIzaSyB544_dW3S7ksRnwkzdAec7bJqwMgcXRZA")

text = st.text_input("enter your questions")

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])


if st.button("Click me"):
    response = chat.send_message(text)
    st.write(response.text)


    