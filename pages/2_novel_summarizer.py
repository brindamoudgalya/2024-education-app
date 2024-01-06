from openai import OpenAI
import streamlit as st

# code for "chatgpt-like clone" copied from streamlit docs:
# https://docs.streamlit.io/knowledge-base/tutorials/build-conversational-apps

st.header("Summarize Any Novel")

client = OpenAI(api_key="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")

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Name a novel/short story/poem to summarize."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        for response in client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        ):
            full_response += (response.choices[0].delta.content or "")
            message_placeholder.markdown("generating summary...")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})