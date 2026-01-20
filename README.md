# zoomcamp-homework-week1

Quick start — terminal commands (use Docker)

Prerequisites:
- Docker / docker-compose available in the devcontainer
- Python 3.13 available in the devcontainer
- wget present on PATH

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

3) Prepare data (download + convert)
```bash
# install minimal runtime deps if needed
python -m pip install --user pandas pyarrow

# prepare files (creates data/*.csv.gz)
python prepare_data.py
```

4) Install ingest dependencies
```bash
python -m pip install --user sqlalchemy psycopg2-binary pandas
```

5) Ingest datasets into Postgres (from host / devcontainer -> postgres mapped to 5433)
```bash
# main dataset
python ingest_data.py \
  --csv data/green_tripdata_2025-11.csv.gz \
  --table green_trips \
  --host localhost --port 5433 --user postgres --password postgres --db ny_taxi

# zones dataset
python ingest_data.py \
  --csv data/taxi_zone_lookup.csv.gz \
  --table taxi_zones \
  --host localhost --port 5433 --user postgres --password postgres --db ny_taxi
```

6) Stop and remove services and volumes
```bash
docker compose down -v
```