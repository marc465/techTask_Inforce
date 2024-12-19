# ETL Pipeline with PostgreSQL and Docker

A technical implementation of an ETL (Extract, Transform, Load) pipeline that processes CSV data and loads it into a PostgreSQL database. The project includes data generation, database initialization, data transformation, and SQL query execution capabilities.

## Features

- Generates random user data with unique email addresses
- Sets up PostgreSQL database with optimized table structure and indexes
- Implements ETL pipeline for data processing
- Executes custom SQL queries for data analysis
- Full Docker containerization
- Handles up to 200,000 unique users

## Prerequisites

- Docker and Docker Compose
- PostgreSQL server
- Python 3.x
- Appropriate database user permissions (CREATE DATABASE and CRUD operations)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/marc465/techTask_Inforce.git
cd techTask_Inforce
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

### Docker Compose Setup

Edit `docker-compose.yml` to configure your environment:

```yaml
db:
  image: postgres:17
  container_name: postgres_db
  environment:
    POSTGRES_DB: your_db_name
    POSTGRES_USER: your_db_user
    POSTGRES_PASSWORD: your_user_password
  ports:
    - "5433:5432"

app:
  build: .
  container_name: python_app
  environment:
    DB_HOST: db
    DB_PORT: 5432
    DB_NAME: your_db_name
    DB_USER: your_db_user
    DB_PASSWORD: your_user_password
    AMOUNT_OF_ROWS: 3000
```

**Important Notes:**
- Ensure your PostgreSQL user has necessary permissions
- The database name 'inforcetaskdb' should not exist prior to running
- Adjust ports if needed ("host_port:container_port")

## Project Structure

- `main.py` - Entry point that orchestrates the ETL process
- `generate_csv.py` - Generates test data with random users
- `init.py` - Initializes database and creates table structure
- `etl_pipeline.py` - Handles the ETL process
- `executeQueries.py` - Executes predefined SQL queries
- `Queries.sql` - Contains SQL queries for data analysis

## Usage

1. Start the application:
```bash
docker compose up --build
```

2. Stop the containers:
```bash
# Press Ctrl+C or run:
docker-compose down
```

## Data Processing Notes

- The system generates unique user data with random names, surnames, and email domains
- Duplicate email handling: When running multiple times, approximately 1.5% of records may be duplicates
- Failed inserts due to duplicate emails are handled gracefully without stopping the process
- Successfully processes all valid data entries

## Database Schema

```sql
CREATE TABLE public.users (
    id bigserial NOT NULL,
    name character varying(64) NOT NULL,
    email character varying(255) NOT NULL,
    signup_date date NOT NULL,
    domain character varying(64) NOT NULL,
    PRIMARY KEY (id),
    UNIQUE (email)
);
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Feel free to submit issues and pull requests.