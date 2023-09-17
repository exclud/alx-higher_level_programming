#!/usr/bin/python3
import MySQLdb
import sys

def list_states():
    """
    Function to list all states from the database hbtn_0e_0_usa
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name=%s ORDER BY id ASC", (sys.argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()

if __name__ == "__main__":
    """
    Main function to prevent execution when imported
    """
    list_states()
