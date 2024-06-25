import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

load_dotenv()

def get_expired_subscription_clients():
    try:
        mydb = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )

        print(f"\nConnected to database: {os.getenv('DB_NAME')}\n")
        mycursor = mydb.cursor(prepared=True)
        query = f"SELECT * FROM {os.getenv('DB_TABLE_NAME')} WHERE {os.getenv('DB_CRITERIA')} < DATE_SUB(CURDATE(), INTERVAL %s DAY)"

        subscription_length = int(input("Enter the subscription lenght: "))
        mycursor.execute(query, (subscription_length,))

        # GET ALL THE ROWS FROM THE EXECUTED COMMAND
        myresult = mycursor.fetchall()

        mycursor.close()
        mydb.close()

    except Error as error:
        print(f"{error}")
        return None

    except Exception as unknown:
        print(f"Unexpected error: {unknown}")
        return None

    return myresult
