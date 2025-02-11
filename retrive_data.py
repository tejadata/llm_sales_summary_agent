from sqlalchemy import create_engine, text
from decimal import Decimal
import json
DB_URI = "postgresql://avnadmin:AVNS_M5AINu9hKrf0KHKphlq@llm-viswatejaster-a9ff.k.aivencloud.com:15452/defaultdb?sslmode=require"
engine = create_engine(DB_URI)

# Convert Decimal to int


def convert_decimal(obj):
    if isinstance(obj, Decimal):
        return int(obj)  # Convert to int
    return obj


def execute_sql_query(sql_query):
    try:
        with engine.connect() as connection:
            result = connection.execute(
                text(sql_query))
            print("---------", result.keys())
            if result:
                rows = result.fetchall()
                columns = result.keys()
                # Convert each row to a dictionary
                rows_dict = [dict(zip(columns, row)) for row in rows]
                print(rows_dict)
                # Return the list of dictionaries
                return json.loads(json.dumps(rows_dict, default=convert_decimal))
            return None
    except Exception as e:
        return {"error": str(e)}
