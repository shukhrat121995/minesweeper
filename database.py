import sqlite3
from sqlite3 import Error, OperationalError


def create_connection(db_file):
    """
    Create a database connection to a SQLite database
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file, isolation_level=None)
        return conn
    except Error as e:
        print(e)


def store_values(played_time, duration, turns, bombs_left, game):
    """
    Store passed values in the stats table
    """
    connection = create_connection('db.db')
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS stats ("
                   "played_time TEXT, "
                   "duration TEXT, "
                   "turns TEXT, "
                   "mines INT, "
                   "game TEXT)")

    cursor.execute(f"INSERT INTO stats VALUES ("
                   f"'{played_time}', "
                   f"'{duration}', "
                   f"'{turns}', "
                   f"{bombs_left}, "
                   f"'{game}')")
    cursor.close()


def retrieve_values():
    """
    Retrieve values from the << stats >> table; return empty list if there are no
    values
    """
    connection = create_connection('db.db')
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM 'stats' ORDER BY played_time ASC;")
    except OperationalError:
        return []
    data = cursor.fetchall()

    return data
