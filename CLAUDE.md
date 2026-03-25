# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Project Is

A local PostgreSQL database for analyzing campus food delivery orders. The data lives in `data/campus_bites_orders.csv` and is loaded into a Dockerized Postgres instance (`campus_bites` database, `orders` table).

## Database Commands

Start the database (detached):
```bash
docker compose up -d
```

Connect via psql:
```bash
docker exec -it campus_bites_db psql -U postgres -d campus_bites
```

Stop (keeps data volume):
```bash
docker compose down
```

Reset everything (destroys data volume):
```bash
docker compose down -v
```

## Connection Details

| Setting  | Value        |
|----------|--------------|
| Host     | localhost    |
| Port     | 5432         |
| Database | campus_bites |
| User     | postgres     |
| Password | postgres     |

## Data Schema

The `orders` table is loaded from `data/campus_bites_orders.csv`:

| Column               | Description                          |
|----------------------|--------------------------------------|
| `order_id`           | Primary key                          |
| `order_date`         | Date of order                        |
| `order_time`         | Time of order                        |
| `customer_segment`   | e.g. Grad Student, Off-Campus        |
| `order_value`        | Dollar amount                        |
| `cuisine_type`       | e.g. Asian, Indian                   |
| `delivery_time_mins` | Delivery duration in minutes         |
| `promo_code_used`    | Yes/No                               |
| `is_reorder`         | Yes/No                               |

## Important Notes

- The `data/` directory is mounted into the container at `/data`. Any table creation or CSV import SQL must reference `/data/campus_bites_orders.csv` inside the container.
- Data is persisted in the named Docker volume `postgres_data`. Dropping and recreating the container (without `-v`) preserves the data.
- There is a `.venv` (Python 3.14) present but no Python scripts yet.
