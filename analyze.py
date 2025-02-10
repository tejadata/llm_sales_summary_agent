from generate_query import generate_sql_query
from retrive_data import execute_sql_query
from summarize_sales import search_sales_reasons
from loss_or_gain import analyze_sales_data


def analyze_sales(question):
    # 1️⃣ Generate SQL
    sql_query = generate_sql_query(question)

    # 2️⃣ Execute Query
    sales_data = execute_sql_query(sql_query)
    print("out from sales dats")
    if not sales_data:
        return "No sales data found."
    print(sales_data)
    # 3️⃣ Extract Product & Region for Internet Search
    first_result = sales_data
    product_name = first_result[0].get("product_name", "medicine")
    region = first_result[0].get("region", "USA")

    loss_gain = analyze_sales_data(sales_data)

    # 4️⃣ Search Internet for Reasons
    market_trends = search_sales_reasons(product_name, region, loss_gain[0])

    # 5️⃣ Return Combined Analysis
    return {
        "sales_data": loss_gain[1],
        "market_trends": market_trends
    }
