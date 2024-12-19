import psycopg2
import time

def run(db_config):
    try:
        connection = psycopg2.connect(**db_config)
        cursor = connection.cursor()
        connection.autocommit = True

        cursor.execute("SELECT 1 FROM pg_database WHERE datname = 'inforcetaskdb'")
        exists = cursor.fetchone()
        
        if not exists:
            cursor.execute("""
                CREATE DATABASE inforcetaskdb;
            """)

        cursor.close()
        connection.close()

        db_config['dbname'] = 'inforcetaskdb'
        connection = psycopg2.connect(**db_config)
        cursor = connection.cursor()

        cursor.execute("""
            BEGIN;

            CREATE TABLE IF NOT EXISTS public.users
            (
                id bigserial NOT NULL,
                name character varying(64) NOT NULL,
                email character varying(255) NOT NULL,
                signup_date date NOT NULL,
                domain character varying(64) NOT NULL,
                PRIMARY KEY (id),
                UNIQUE (email)
            );

            CREATE INDEX IF NOT EXISTS idx_email ON public.users (email);
            CREATE INDEX IF NOT EXISTS idx_name ON public.users (name);
            CREATE INDEX IF NOT EXISTS idx_domain ON public.users (domain);

            COMMIT;
        """)

        print("Database and tables were created successfully!")
        
    except Exception as e:
        print("Error: ", e)
        if connection:
            connection.rollback()

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()