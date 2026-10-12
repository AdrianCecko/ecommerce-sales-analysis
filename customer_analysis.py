import os

import pandas as pd
from sqlalchemy import create_engine, URL
import matplotlib.pyplot as plt
from dotenv import load_dotenv

def classify_customer(order_count):

    if order_count > 1:
        return "returning"
    elif order_count == 1:
        return "one time"
    else:
        return "inactive"
load_dotenv()
db_url = URL.create(
    drivername="postgresql+psycopg",
    username=os.environ["DB_USER"],
    password=os.environ["DB_PASSWORD"],
    host=os.environ["DB_HOST"],
    port=int(os.environ["DB_PORT"]),
    database=os.environ["DB_NAME"]
)
engine = create_engine(db_url)

orders = pd.read_sql_query("SELECT * FROM orders", engine)
customers = pd.read_sql_query("SELECT * FROM customers", engine)

merge = pd.merge(customers, orders, on="customer_id", how="left")

revenue = (
    merge.groupby(["customer_id","name"])
    .agg(
        total_spent=("amount", "sum"),
        total_count=("order_id","count")
    ).reset_index()

)
revenue = revenue.sort_values(
    by="total_spent",
    ascending=False
)
print(revenue)
print(revenue.isna().sum())
print("BREAK")
print("total spent:")
print(revenue["total_spent"].sum())
print("total count:")
print(revenue["total_count"].sum())
revenue.to_csv("customer_report_csv", index=False)

revenue["customer_type"] = revenue["total_count"].apply(classify_customer)

print(revenue)





