# E-commerce Sales Analysis

A beginner data analytics project using **Python, PostgreSQL, Pandas, and Matplotlib**.

The project demonstrates how to connect Python to a PostgreSQL database, retrieve sales data using SQL, process it with Pandas, and visualize monthly revenue.

## Technologies Used

- **Python** – data processing and analysis
- **PostgreSQL** – relational database for storing sales data
- **SQLAlchemy & Psycopg** – database connectivity
- **Pandas** – data manipulation and aggregation
- **Matplotlib** – data visualization
- **python-dotenv** – environment variable management

## Project Workflow

1. Connect to a local PostgreSQL database using SQLAlchemy.
2. Retrieve order data with a SQL query (`SELECT * FROM orders`).
3. Load the results into a Pandas DataFrame.
4. Convert the `order_date` column to a datetime format.
5. Group orders by month and calculate total monthly revenue.
6. Generate a bar chart showing monthly sales revenue.

## Sample Analysis Results

Based on the sample dataset:

| Month | Total Revenue (PLN) |
|---|---:|
| January 2025 | 650 |
| February 2025 | 1,050 |
| March 2025 | 750 |

February generated the highest revenue in the sample dataset.

These results are based on fictional data and are intended for educational purposes.

## How to Run

**1. Clone the repository**

```bash
git clone https://github.com/AdrianCecko/ecommerce-sales-analysis.git
```

**2. Install dependencies**

```bash
pip install -r requirements.txt
```

**3. Configure PostgreSQL**

Create a PostgreSQL database named `sales_analysis` with an `orders` table containing:

- `order_id`
- `customer_id`
- `order_date`
- `amount`

Populate the table with sample sales records.

**4. Create a `.env` file**

```dotenv
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=sales_analysis
```

**5. Run the analysis**

```bash
python main.py
```

The application will retrieve sales records, calculate monthly revenue, and display a bar chart.

## Future Improvements

- Customer segmentation and revenue analysis
- Data cleaning and validation
- Additional sales KPIs
- Interactive dashboards using Power BI
- Analysis of larger datasets

## Project Status

**Work in progress** – developed as a hands-on learning project to strengthen SQL, Python, and data analytics skills.
