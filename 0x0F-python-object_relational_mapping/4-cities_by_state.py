#!/usr/bin/python3
"""  lists all cities from the database hbtn_0e_4_usa along with their
    respective states"""
import MySQLdb
import sys


def main():
    """
    Connects to a MySQL database and lists all cities along with their
        corresponding states.

    Usage:
        python script.py <username> <password> <database_name>
    """
    db_connection = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                                    db=sys.argv[3])

    cursor = db_connection.cursor()

    cursor.execute("""SELECT cities.id, cities.name, states.name FROM cities
                   JOIN states ON states.id=cities.state_id""")
    result = cursor.fetchall()
    for row in result:
        print(row)

    cursor.close()
    db_connection.close()


if __name__ == "__main__":
    main()
