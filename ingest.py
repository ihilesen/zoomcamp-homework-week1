import pandas as pd
from sqlalchemy import create_engine
import sys

DB_URL = "postgresql://postgres:postgres@db:5432/ny_taxi"

def ingest_parquet(file_path, table_name):
    engine = create_engine(DB_URL)

    df = pd.read_parquet(file_path)
    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False,
        chunksize=100_000
    )

    print(f"Ingested {len(df)} rows into {table_name}")

if __name__ == "__main__":
    ingest_parquet(sys.argv[1], "green_tripdata")