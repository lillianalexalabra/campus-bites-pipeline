# Campus Bites Pipeline

Local PostgreSQL database for analyzing campus food delivery orders.

## Requirements

- [Docker Desktop](https://www.docker.com/products/docker-desktop/)

## Setup

1. Clone the repo and navigate into it:
   ```bash
   git clone <your-repo-url>
   cd campus-bites-pipeline
   ```

2. Start the database:
   ```bash
   docker compose up -d
   ```

   Postgres will start and automatically create the `orders` table and load the CSV data. This only runs once — data is persisted in a Docker volume.

3. Connect and query:

   **Option A — psql (command line):**
   ```bash
   docker exec -it campus_bites_db psql -U postgres -d campus_bites
   ```

   **Option B — GUI (TablePlus, DBeaver, DataGrip, etc.):**
   | Setting  | Value        |
   |----------|--------------|
   | Host     | localhost    |
   | Port     | 5432         |
   | Database | campus_bites |
   | User     | postgres     |
   | Password | postgres     |

## Example Queries

```sql
-- Preview the data
SELECT * FROM orders LIMIT 10;

-- Average order value by cuisine type
SELECT cuisine_type, ROUND(AVG(order_value), 2) AS avg_value
FROM orders
GROUP BY cuisine_type
ORDER BY avg_value DESC;

-- Orders with promo codes by customer segment
SELECT customer_segment, COUNT(*) AS promo_orders
FROM orders
WHERE promo_code_used = true
GROUP BY customer_segment;
```

## Teardown

Stop the container (keeps data):
```bash
docker compose down
```

Stop and delete all data:
```bash
docker compose down -v
```
