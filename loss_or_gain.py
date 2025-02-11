#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 20:01:31 2025

@author: bhanuteja
"""

import groq
import os
# 🔹 Initialize Groq Client
client = groq.Client(
    api_key=os.environ["api_key"]
)


def analyze_sales_data(sales_data):
    print("Analyzing loss or gain")

    prompts = [
        """
        Please calculate the loss or gain from the columns total_sales for JAN and FEB just give either gain or loss nothing else
        
        {sales_data}
        
        Provide a short and precise summary.
        """,
        """
        Please calculate the loss or gain from the columns total_sales for JAN and FEB 
        
        {sales_data}
        
        Provide a short and precise summary.
        """
    ]

    results = []
    for prompt in prompts:
        response = client.chat.completions.create(
            model="gemma2-9b-it",
            top_p=1,
            temperature=0,
            messages=[
                {"role": "user", "content": prompt.format(sales_data=sales_data)}],
        )
        results.append(response.choices[0].message.content.strip())

    return results
