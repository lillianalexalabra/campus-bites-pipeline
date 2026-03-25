import pandas as pd
from sqlalchemy import create_engine, text

# Connection string for the local Postgres container defined in docker-compose.yml.
# Format: postgresql://user:password@host:port/database
DB_URL = "postgresql://postgres:postgres@localhost:5432/campus_bites"
CSV_PATH = "data/campus_bites_orders.csv"

# Create a SQLAlchemy engine, which manages the connection pool to Postgres.
# The underlying driver is psycopg2.
engine = create_engine(DB_URL)

# Create the orders table if it doesn't already exist.
# IF NOT EXISTS makes this safe to run multiple times without error.
with engine.connect() as conn:
    conn.execute(text("""
        CREATE TABLE IF NOT EXISTS orders (
            order_id            INTEGER PRIMARY KEY,
            order_date          DATE,
            order_time          TIME,
            customer_segment    TEXT,
            order_value         NUMERIC(10, 2),
            cuisine_type        TEXT,
            delivery_time_mins  INTEGER,
            promo_code_used     TEXT,
            is_reorder          TEXT
        )
    """))
    conn.commit()

# Load the CSV into a pandas DataFrame.
# pandas reads the header row automatically to name the columns.
df = pd.read_csv(CSV_PATH)

# Append the DataFrame rows into the orders table.
# if_exists="append" adds rows to the existing table without dropping it.
# index=False prevents pandas from writing its own row index as an extra column.
df.to_sql("orders", engine, if_exists="append", index=False)

print(f"Loaded {len(df)} rows into orders table.")
