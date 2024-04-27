import mysql.connector
from mysql.connector import Error

# Define host name, user name, user password, and database to be used
HOST = "localhost"
NAME = "root"
PW = "walangpassword"
DB = "lab5"

""""""

def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

def main():
    connection = create_db_connection(HOST, NAME, PW, DB)

if __name__ == "__main__":
    main()