import streamlit as st
import requests
import os
from dotenv import load_dotenv
load_dotenv()
os.environ["STREAMLIT_BROWSER_GATHER"] = "false"
os.environ["BROWSER"]="none"
GROQ_API_KEY=os.getenv("GROQ_API_KEY")
API_URL="https://api.groq.com/openai/v1/chat/completions"
def chat_with_groq(messages,model="meta-llama/llama-4-scout-17b-16e-instruct",temperature=0.7):
    headers={
        'Authorization':f'Bearer {GROQ_API_KEY}',
        'Content-Type':'application/json'
    }
    payload={
        "model":model,
        "messages":messages,
        "temperature":temperature
    }
    response=requests.post(API_URL,headers=headers,json=payload)
    if response.status_code==200:
        result=response.json()
        reply=result['choices'][0]['message']['content']
        return reply
    else:
        return f"Error{response.status_code}:{response.text}"
st.title("AI Chatbot Powered by Groq LLM")
st.caption("Built with LLaMA 4 Scout via Groq API")
if "messages" not in st.session_state:
    st.session_state.messages=[{"role":"system","content":"You are a helpful AI chatbot."}]
for message in st.session_state.messages[1:]:
    if message["role"]=="user":
        st.write(f"You: {message['content']}")
    else:
        st.write(f"Bot: {message['content']}")
user_input=st.text_input("Your message:",key="user_input")
if st.button("Send"):
    if user_input:
        st.session_state.messages.append({"role":"user","content":user_input})
        response=chat_with_groq(st.session_state.messages)
        st.session_state.messages.append({"role":"assistant","content":response})
        st.rerun()