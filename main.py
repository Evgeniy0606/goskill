import streamlit as st
import random
import time

st.write("Streamlit loves LLMs! 🤖 [Build your own chat app](https://docs.streamlit.io/develop/tutorials/llms/build-conversational-apps) in minutes, then make it powerful by adding images, dataframes, or even input widgets to the chat.")

st.caption("Note that this demo app isn't actually connected to any LLMs. Those are expensive ;)")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Let's start chatting! 👇"}]

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    prompt = prompt.strip().split(" ")
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        if len(prompt) != 3:
            st.markdown("ВВЕДИТЕ ЧИСЛО ОПЕРАТОР ЧИСЛО")
        else:
            if prompt[1] == "+":
                full_response = int(prompt[0]) + int(prompt[2])
            if prompt[1] == "-":
                full_response = int(prompt[0]) - int(prompt[2])
            if prompt [1] == "*":
                full_response = int(prompt[0]) * int(prompt[2])
            if prompt [1] == "/":
                full_response = int(prompt[0]) / int(prompt[2])
            st.markdown(int(full_response))
            st.session_state.messages.append({"role": "assistant", "content": int(full_response)})