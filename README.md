# zoomcamp-homework-week1

Quick start — terminal commands (use Docker)

Prerequisites:
- Docker / docker-compose available in the devcontainer
- Python 3.13 available in the devcontainer
- wget present on PATH

check pip version
```
docker run -it --rm --entrypoint bash python:3.13
pip --version
```
1) Start services (recommended)
```bash
docker compose up -d
```

Or run a single Postgres container:
```bash
# make executable and run: ./docker\ run
./docker\ run
```

2) Open pgAdmin in host browser
```bash
$BROWSER http://localhost:8080
# login: pgadmin@pgadmin.com / pgadmin
```

3) Install dependencies
```bash
python -m pip install --user sqlalchemy psycopg2-binary pandas pyarrow pgcli
```

4) Ingest datasets into Postgres
```bash
# green tripdata (parquet format)
python ingest.py data/raw/green_tripdata_2025-11.parquet

# taxi zones (CSV format)
python -c "
import pandas as pd
from sqlalchemy import create_engine
DB_URL = 'postgresql://postgres:postgres@localhost:5433/ny_taxi'
engine = create_engine(DB_URL)
df = pd.read_csv('data/raw/taxi_zone_lookup.csv')
df.to_sql('taxi_zone_lookup', engine, if_exists='replace', index=False)
print(f'Ingested {len(df)} rows into taxi_zone_lookup')
"
```

5) Access the database

**pgAdmin (GUI)** - Open http://localhost:8080
- Login: pgadmin@pgadmin.com / pgadmin
- Database: ny_taxi (postgres:postgres@localhost:5433)

**pgcli (CLI)** - Interactive SQL shell
```bash
pgcli postgresql://postgres:postgres@localhost:5433/ny_taxi
```

**Python** - Programmatic access
```python
from sqlalchemy import create_engine
engine = create_engine('postgresql://postgres:postgres@localhost:5433/ny_taxi')
df = pd.read_sql('SELECT * FROM green_tripdata LIMIT 5', engine)
```

6) Stop and remove services and volumes
```bash
docker compose down -v
```

## Ingested Tables

- **green_tripdata** (46,912 rows) - Green taxi trip data with columns: VendorID, lpep_pickup_datetime, lpep_dropoff_datetime, store_and_fwd_flag, RatecodeID, PULocationID, DOLocationID, passenger_count, trip_distance, fare_amount, extra, mta_tax, tip_amount, tolls_amount, ehail_fee, improvement_surcharge, total_amount, payment_type, trip_type, congestion_surcharge, cbd_congestion_fee

- **taxi_zone_lookup** (265 rows) - Taxi zone reference table with columns: LocationID, Borough, Zone, service_zone