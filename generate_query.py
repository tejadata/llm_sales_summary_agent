from sqlalchemy import create_engine, text
import os
import groq
from prompts import prompts

import streamlit as st

# 🔹 Initialize Groq Client
client = groq.Client(
    api_key=st.secrets["api_keys"]["api_key"]
)


def generate_sql_query(user_question):
    """Generate SQL query """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        top_p=0,
        temperature=0,
        messages=[{"role": "user", "content": prompts(user_question)}],
    )

    sql_query = response.choices[0].message.content
    print("======generated query=============")
    print(sql_query)
    return sql_query.strip()
