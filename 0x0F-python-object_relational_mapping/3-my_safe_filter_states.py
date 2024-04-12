#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa where name matches
    the argument that is safe from MySQL injections"""

import MySQLdb
import sys


def main():
    """
    Connects to a MySQL database and lists states where the name matches
    the argument provided, ensuring safety from MySQL injections.

    Usage:
        python script.py <username> <password> <database_name> <state_name>
    """
    db_connection = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                                    db=sys.argv[3])

    cursor = db_connection.cursor()

    search_states = sys.argv[4]

    cursor.execute("SELECT * FROM states WHERE name=%s", (search_states, ))
    result = cursor.fetchall()
    for row in result:
        print(row)

    cursor.close()
    db_connection.close()


if __name__ == "__main__":
    main()
