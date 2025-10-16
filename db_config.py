import mysql.connector


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # change if different
        password="revanth",  # use your MySQL root password
        database="expense_tracker"
    )
