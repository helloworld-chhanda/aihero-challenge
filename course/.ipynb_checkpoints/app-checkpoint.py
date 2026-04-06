import streamlit as st
import asyncio
import time

import ingest
import search_agent
import logs


# --- Page config FIRST ---
st.set_page_config(
    page_title="AI FAQ Assistant",
    page_icon="🤖",
    layout="centered"
)

st.write("VERSION: CLEAN CODE v3")


# --- Initialization ---
@st.cache_resource(show_spinner=False)
def init_agent():
    repo_owner = "DataTalksClub"
    repo_name = "faq"

    def filter(doc):
        return "data-engineering" in doc["filename"]

    index = ingest.index_data(repo_owner, repo_name, filter=filter)
    agent = search_agent.init_agent(index, repo_owner, repo_name)
    return agent


with st.spinner("🔄 Indexing repo..."):
    agent = init_agent()


# --- UI ---
st.title("🤖 AI FAQ Assistant")
st.caption("Ask me anything about the DataTalksClub/faq repository")


# --- Chat history ---
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


# ✅ --- FUNCTIONS MUST BE HERE (before usage) ---

def get_response(prompt: str):
    result = asyncio.run(agent.run(user_prompt=prompt))
    logs.log_interaction_to_file(agent, result.new_messages())
    return result.output


def fake_stream(text: str):
    for word in text.split():
        yield word + " "
        time.sleep(0.02)


# --- Chat input ---
if prompt := st.chat_input("Ask your question..."):

    # User message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Assistant response
    with st.chat_message("assistant"):
        full_response = get_response(prompt)
        st.write_stream(fake_stream(full_response))

    # Save response
    st.session_state.messages.append(
        {"role": "assistant", "content": full_response}
    )