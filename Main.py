import os 
from constants import openai_key
from langchain_community.llms import openai as OpenAI

import streamlit as st

#Streamlit framework

st.title('Lamgchain Demo With OPENAI API')
input_text=st.text_input("Search the topic u want")

st.text_area("Hello Everyone !!")

# os.environ["OPENAI_API_KEY"] = openai_key

# ## OPENAI LLMS

# llm = OpenAI.OpenAI(temperature=0.8)

# if input_text:
#     st.write(llm(input_text))