import pyodbc
import os


def db_connect():
    """
    Connect to docker MSSQL container db
    :return:
    """
    drivers = [item for item in pyodbc.drivers()]
    driver = drivers[-1]

    conn = pyodbc.connect(f'Driver={driver};'
                          f'Server={os.environ["DB_SERVER"]};'
                          f'Port={os.environ["DB_PORT"]};'
                          f'Database={os.environ["DB_NAME"]};'
                          f'UID={os.environ["DB_USER"]};'
                          f'PWD={os.environ["DB_PASS"]};')
    return conn
