import psycopg2

def run(db_config):
    try:
        db_config['dbname'] = 'inforcetaskdb'
        connection = psycopg2.connect(**db_config)
        cursor = connection.cursor()    
    except Exception as e:
        print("Error while connecting to DataBase: ", e)

    try:
        with open("./db/Queries.sql", "rt") as file:
            queries = file.read().split("\n\n")
            for query in queries:
                cursor.execute(query)
                connection.commit()

                if "DELETE" in query:
                    print(cursor.rowcount)
                    continue

                results = cursor.fetchall()
                
                if results:
                    for row in results:
                        print(row)
                    print()
                else:
                    print("No results found")
                    print()

    except Exception as e:
        print("Error occured: ", e)
    
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
        print("Connection closed")
