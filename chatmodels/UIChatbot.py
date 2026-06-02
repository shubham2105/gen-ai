import streamlit as st
from dotenv import load_dotenv

from langchain_mistralai.chat_models import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

load_dotenv()

# Initialize model
model_mistral = ChatMistralAI(model="devstral-2512")

# Session state to store messages (required in Streamlit)
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="You are a funny Ai Agent")
    ]

st.title("Mistral Chatbot")

st.write("Type '0' to exit")

# Display chat history (excluding system message)
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        st.chat_message("user").write(msg.content)
    elif isinstance(msg, AIMessage):
        st.chat_message("assistant").write(msg.content)

# User input
prompt = st.chat_input("You:")

if prompt:
    if prompt == "0":
        st.stop()

    # Append user message
    st.session_state.messages.append(HumanMessage(content=prompt))
    st.chat_message("user").write(prompt)

    # Get response
    response_mistral = model_mistral.invoke(st.session_state.messages)

    # Append AI message
    st.session_state.messages.append(
        AIMessage(content=response_mistral.content)
    )

    st.chat_message("assistant").write(response_mistral.content)