import os
from dotenv import load_dotenv
import psycopg2
from psycopg2 import Error

load_dotenv()

def get_db_connection():
    try:
        conn = psycopg2.connect(dsn=os.getenv('DATABASE_URL'))
        print("Connection successful")
        return conn
    
    except Error as e:
        print(f"Could not connect to the database. Error - {e}")
        return None

if __name__ == "__main__": 
    print("Testing database connection...")
    test_conn = get_db_connection()

    if test_conn:
        cur = test_conn.cursor()
        cur.execute("SELECT version();")
        version = cur.fetchone()[0]
        print(f"DB Version - {version}")

        cur.close()
        test_conn.close()
        print("Ping test complete. Connection closed.")