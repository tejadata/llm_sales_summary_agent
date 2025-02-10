from duckduckgo_search import DDGS
import groq

# 🔹 Initialize Groq Client
client = groq.Client(
    api_key="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")


def search_sales_reasons(product_name, region, loss_gain):
    """Fetches and summarizes reasons for low sales of a product in a region."""
    query = f"Why are {product_name} sales down in {region} 2025?"
    print("Search Query:", query)

    # Fetch search results
    with DDGS() as ddgs:
        search_results = list(ddgs.text(query, max_results=5))

    # Extract relevant text from search results
    extracted_texts = [
        f"{res['title']}: {res['body']}" for res in search_results]

    # Combine results into a single text for summarization
    combined_text = "\n".join(extracted_texts)

    # Summarize using Llama via Groq
    summary_prompt = f"""
    Summarize the key reasons for the {loss_gain} in {product_name} sales in {region} based on these sources also removde special charecters:
    
    {combined_text}
    
    Provide a short and precise summary.
    """

    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[{"role": "user", "content": summary_prompt}],
    )

    summary = response.choices[0].message.content.strip()

    return summary
