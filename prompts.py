def prompts(user_question):
    prompt = f"""Generate a single SQL query to retrieve the total sales from the med_sales table based on the user’s question:
                User Question: “{user_question}”

                Do not include any explanation. Only return a valid SQL query. Do not include triple backticks (```).

                Table Schema:
                    •	product_name (TEXT)
                    •	category (TEXT)
                    •	region (TEXT)
                    •	quantity_sold (INTEGER)
                    •	price (DECIMAL)
                    •	sale_date (TEXT)

                Query Requirements:
                    •	If the user asks about a product_name, generate a query that filters using WHERE product_name = '...' AND region = '...'.
                    •	If the user asks about a category, generate a query that filters using WHERE category = '...' AND region = '...'.
                    •	The query should always include sale_date in the GROUP BY clause, regardless of whether the user asks about product_name or category.
                    •	The query should calculate total sales using SUM(quantity_sold * price).
                    •	The query should include GROUP BY based on the user’s input (product_name or category), and that field should also be included in the SELECT clause.
                    •	Do not generate two separate queries.
                    •	The query should always include sale_date in the GROUP BY clause, regardless of whether the user asks about product_name or category."""

    return prompt
