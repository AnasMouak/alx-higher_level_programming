#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


def main():
    """
    Connects to a MySQL database using provided credentials and fetches
    all rows from the 'states' table.

    Usage:
        python script.py <username> <password> <database_name>
    """
    db_connection = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                                    db=sys.argv[3])

    cursor = db_connection.cursor()

    cursor.execute("SELECT * FROM states")
    result = cursor.fetchall()
    for row in result:
        print(row)

    cursor.close()
    db_connection.close()


if __name__ == "__main__":
    main()
