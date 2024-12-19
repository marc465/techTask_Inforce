import csv
import psycopg2
from datetime import datetime

def transformDate(date:str):
    dt = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
    return str(dt.date())

def extractDomain(email:str):
    return email.split("@")[1]

def run(db_config):
    try:
        db_config['dbname'] = 'inforcetaskdb'
        connection = psycopg2.connect(**db_config)
        cursor = connection.cursor()
        
    except Exception as e:
        print("Error while connecting to DataBase: ", e)
        
    try:
        with open("./data/data.csv", "rt") as file:
            csvreader = csv.reader(file)

            fields = next(csvreader)
            for row in csvreader:
                cursor.execute("""
                    INSERT INTO public.users (name, email, signup_date, domain)
                    VALUES (%s, %s, %s, %s);
                """, (row[1], row[2], transformDate(row[3]), extractDomain(row[2])))
                connection.commit()

        print("Data has been read, transformed and inserted into DataBase successfully!")

    except Exception as e:
        print("Error: ", e)

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
