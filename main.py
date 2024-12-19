from src import generate_csv, etl_pipeline
from db import init, executeQueries
import os

db_config = {
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
}

amout_of_rows = os.getenv("AMOUNT_OF_ROWS")

if __name__ == "__main__":
    generate_csv.run(int(amout_of_rows))
    init.run(db_config)
    etl_pipeline.run(db_config)
    executeQueries.run(db_config)

    print("ETL pipeline app completed its work")
