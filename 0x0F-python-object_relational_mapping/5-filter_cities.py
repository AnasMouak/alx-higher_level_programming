#!/usr/bin/python3
"""  lists all cities from the database hbtn_0e_4_usa where name of the state
    matches the argument"""
import MySQLdb
import sys


def main():
    """
    Connects to a MySQL database and lists all cities where the state name
    matches the argument.

    Usage:
        python script.py <username> <password> <database_name> <state_name>
    """
    db_connection = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                                    db=sys.argv[3])

    cursor = db_connection.cursor()

    name_state = sys.argv[4]

    cursor.execute("""SELECT cities.name FROM cities
                   JOIN states ON states.id=cities.state_id
                   WHERE states.name=%s""", (name_state, ))

    result = cursor.fetchall()
    for i, row in enumerate(result):
        if i != 0:
            print(", ", end="")
        print(row[0], end="")
    print()
    cursor.close()
    db_connection.close()


if __name__ == "__main__":
    main()
