from database import db_connect

TEST_VAL = [
    (1, 3),  (2, 10), (3, 5),
    (4, 12), (5, 2),  (6, 8),
    (7, 7),  (8, 1),  (9, 15)
]


def populate_test_data(conn, table, test_val):
    """
    Populate testDB with test values (int ascending, rand int)
    :param conn: db connection object returned by db.db_connect()
    :param table: string of table name for input values
    :param test_val: list of tuples (global) containing test values

    :return:
    """
    cursor = conn.cursor()
    for item in test_val:
        cursor.execute(f"INSERT INTO {table} VALUES ({item[0]}, {item[1]})")


if __name__ == '__main__':
    populate_test_data(db_connect(), "Tasks", TEST_VAL)
