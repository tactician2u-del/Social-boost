import streamlit as st
from textblob import TextBlob
import pandas as pd
import plotly.express as px
from datetime import datetime
import io
from docx import Document

st.set_page_config(page_title="SocialBoost AI Chatbot", layout="wide")
st.title("🚀 SocialBoost AI — Chatbot for Social Media Campaigns")
st.markdown("**Reach • Engagement • Positive Sentiment Booster**")

# Sidebar — Campaign Setup
with st.sidebar:
    st.header("📋 Campaign Setup")
    campaign_name = st.text_input("Campaign Name", "Election Sentiment Drive 2026")
    platforms = st.multiselect("Platforms", ["X (Twitter)", "Instagram", "LinkedIn", "Facebook", "TikTok"], default=["X (Twitter)", "Instagram"])
    audience = st.text_input("Target Audience", "Young voters, urban & rural")
    goal = st.selectbox("Main Goal", ["Increase positive sentiment", "Maximize reach", "Boost engagement", "Drive shares/comments"])
    st.caption("AI will tailor every response to these settings")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": f"Hi! I'm SocialBoost AI for **{campaign_name}**. How can I help boost your reach, engagement, and positive sentiment today? 🎯"}
    ]

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
if prompt := st.chat_input("Ask anything about your campaign..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = "I'm here to help! Tell me more about your campaign or paste a post for sentiment analysis."
            st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})

st.caption("Refresh page for new session • Built by Uma • Powered by Grok")￼Enter
