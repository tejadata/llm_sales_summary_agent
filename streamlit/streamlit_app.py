import streamlit as st
import requests

# API Endpoint (Replace with your actual API URL)
API_URL = "https://llm-sales-summary-agent.onrender.com/summerize"

# Set Streamlit page config
st.set_page_config(page_title="💬 Sales Chatbot", layout="wide")

st.title("💬 AI Sales Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.chat_input("Ask about sales data or market trends...")

if user_input:
    # Display user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Call the API
    response = requests.post(API_URL, json={"value": user_input})

    if response.status_code == 200:
        data = response.json()  # Parse response

        # Extract sales data & market trends
        sales_data = data.get("sales_data", "No sales data available.")
        market_trends = data.get(
            "market_trends", "No market trends available.")

        # Format response
        bot_reply = f"**💰 Sales Data:**\n> {sales_data}\n\n**📈 Market Trends:**\n{market_trends}"

    else:
        bot_reply = "⚠️ Error: Unable to fetch data."

    # Display bot response
    st.session_state.messages.append(
        {"role": "assistant", "content": bot_reply})
    with st.chat_message("assistant"):
        st.markdown(bot_reply)
