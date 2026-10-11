import os

import pandas as pd
from sqlalchemy import create_engine, URL
import matplotlib.pyplot as plt
from dotenv import load_dotenv

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

orders = pd.read_sql("SELECT * FROM orders", engine)
customers = pd.read_sql("SELECT * FROM customers", engine)

orders["order_date"] = pd.to_datetime(orders["order_date"])

monthly = (
    orders.groupby(orders["order_date"].dt.to_period("M"))["amount"]
    .sum()
)
monthly.plot(kind="bar")

plt.title("Monthly revenue")
plt.xlabel("Month")
plt.ylabel("Revenue PLN")
plt.tight_layout()
plt.show()
