#!/usr/bin/python3
import MySQLdb
import sys

def list_cities():
    """
    Function to list all cities from a state in the database hbtn_0e_4_usa
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities \
                 JOIN states ON cities.state_id = states.id \
                 WHERE states.name=%s ORDER BY cities.id ASC", (sys.argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()

if __name__ == "__main__":
    """
    Main function to prevent execution when imported
    """
    list_cities()
