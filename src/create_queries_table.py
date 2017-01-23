#!/usr/bin/python
import argparse
import os
import sqlite3

def run(db_name):
    if not db_name.endswith('.db'):
        raise Exception('DB name must end with .db')

    conn = sqlite3.connect(db_name)

    cursor = conn.cursor()

    # status can have 0 (pending) , 1 (finished) or 2 (error)
    # if error is set, blob contains the error message

    querystr = """CREATE TABLE queries (
        id integer primary key autoincrement,
        username string,
        query string,
        status number,
        result blob        
        )"""

    cursor.execute(querystr)

    querystr = """CREATE TRIGGER xenon_query
        AFTER INSERT ON queries 
        BEGIN SELECT xenon_query(NEW.id, NEW.query); 
        end;"""

    cursor.execute(querystr)

    conn.commit()

    conn.close()


def argument_parser():
    # define argument menu
    description = "Creates a SQLite DB database file (or inserts table) with queries and results of queries"
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-n', '--name', default='', help='DB name (must end with .db)', type=str, required=True)
    return parser


def main():
    try:
        arguments = argument_parser().parse_args()
        run(arguments.name)
    except Exception as exception:
        print(exception)

if __name__ == "__main__":
    main()
