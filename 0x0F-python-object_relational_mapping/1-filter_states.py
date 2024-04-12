#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa where the state name starts
with 'N'.
"""
import MySQLdb
import sys


def main():
    """
    Connects to a MySQL database using provided credentials and fetches states
        where the name starts with 'N'.

    Usage:
        python script.py <username> <password> <database_name>
    """
    db_connection = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                                    db=sys.argv[3])

    cursor = db_connection.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%'")
    result = cursor.fetchall()
    for row in result:
        print(row)

    cursor.close()
    db_connection.close()


if __name__ == "__main__":
    main()
