import streamlit as st
import requests
import time

# API Endpoint (Replace with your actual API URL)
API_URL = "https://llm-sales-summary-agent.onrender.com/summerize"
# API_URL = "http://localhost:8000/summerize"

# Set Streamlit page config
st.set_page_config(
    page_title="💬 AI Sales Chatbot by TejawithData", layout="wide")

# Custom CSS for better UI
st.markdown("""
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #F0F2F6;
        }
        .stChatInput {
            font-size: 18px;
        }
        .stButton>button {
            background-color: #0078D7;
            color: white;
            font-size: 18px;
            padding: 12px 24px;
            border-radius: 8px;
            border: none;
        }
        .stButton>button:hover {
            background-color: #005EA6;
        }
        .user-msg {
            background-color: #0078D7;
            color: white;
            padding: 12px 16px;
            border-radius: 12px;
            margin: 8px 0;
            width: fit-content;
            max-width: 80%;
        }
        .bot-msg {
            background-color: #E8E8E8;  /* Light gray */
            color: black;
            padding: 12px 16px;
            border-radius: 12px;
            margin: 8px 0;
            width: fit-content;
            max-width: 80%;
        }
        .typing {
            color: #777;
            font-style: italic;
            padding: 8px;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar for Chatbot instructions
with st.sidebar:
    st.image("https://img.icons8.com/color/100/robot.png")  # Chatbot Icon
    st.title("💬 AI Sales Chatbot")
    st.write("🚀 Ask me about sales data or market trends!")
    st.write("📊 Medicine Category:")
    st.markdown(
        "- Analgesic, Anti-inflammatory, Antibiotic, Antihistamine, Diabetes ")
    st.write("📊 Medicine Sales Region:")
    st.markdown("- East, West, North, south")
    st.write("📊 Sample Question:")
    st.markdown("- **What are the total sales of Analgesic in North?**")
    st.markdown("- what are the total sales of Antibiotic in North?")

st.title("💬 AI Sales Chatbot by TejaWithdata")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history with better formatting
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        if message["role"] == "user":
            st.markdown(
                f'<div class="user-msg">{message["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(
                f'<div class="bot-msg">{message["content"]}</div>', unsafe_allow_html=True)

# User input
user_input = st.chat_input("Ask about sales data or market trends...")

if user_input:
    # Display user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(
            f'<div class="user-msg">{user_input}</div>', unsafe_allow_html=True)

    # Simulate bot "typing..."
    with st.chat_message("assistant"):
        typing_placeholder = st.empty()
        typing_placeholder.markdown(
            '<div class="typing">🤖 Analyzing your question...</div>', unsafe_allow_html=True)
        time.sleep(1.5)  # Simulate delay for a more human-like feel

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

    # Remove typing effect and show the actual response
    typing_placeholder.empty()

    # Display bot response
    st.session_state.messages.append(
        {"role": "assistant", "content": bot_reply})
    with st.chat_message("assistant"):
        st.markdown(
            f'<div class="bot-msg">{bot_reply}</div>', unsafe_allow_html=True)
