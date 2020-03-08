import pyodbc
import os


def db_connect():
    """
    TODO: connect to docker MSSQL container db
    :return:
    """
    conn = pyodbc.connect(f'Driver={os.environ["SQL_DRIVER"]};'
                          f'Server={os.environ["DB_SERVER"]};'
                          f'Port={os.environ["DB_PORT"]};'
                          f'Database={os.environ["DB_NAME"]};'
                          f'UID={os.environ["DB_USER"]};'
                          f'PWD={os.environ["DB_PASS"]};')
    return conn
