#!/usr/bin/python
import argparse
import os
import json
import sqlite3


def parse_node(node=None, cursor=None, tablename=None, is_instance=None, child_of=None, level=None ):
    """
        this function recursively calls itself on its instances or children, if there are any.
    """

    if 'children' in node.keys():
        child_count = len(node['children'])
    else:
        child_count = 0

    if 'instances' in node.keys():
        instance_count = len(node['instances'])
    else:
        instance_count = 0

    if 'mention_count' in node.keys():
        mention_count = node['mention_count']
    else:
        mention_count = 0

    if child_of is None:
        parent_id = -1
    else:
        name = node['name']
        cursor.execute('INSERT INTO ' + tablename + ' ' +
                       '(name, isinstance, childof, childcount, instancecount, mentioncount) VALUES (?,?,?,?,?,?)',
                       (name, 1 if is_instance is True else 0, child_of, child_count, instance_count, mention_count))
        parent_id = cursor.lastrowid

    if is_instance:
        return None
    else:
        # fire off recursive calls
        if child_count > 0:
            # It has children
            for child in node['children']:
                print(level * '    ', child['name'])
                parse_node(node=child, cursor=cursor, tablename=tablename, is_instance=False,
                           child_of=parent_id, level=level + 1)
        if instance_count > 0:
            # It has instances
            for instance in node['instances']:
                print(level * '    ', instance['name'], '(i)')
                parse_node(node=instance, cursor=cursor, tablename=tablename, is_instance=True,
                           child_of=parent_id, level=level + 1)

        return None





def run(input_json, db_name, tablename):
    if not os.path.isfile(input_json):
        raise Exception('File not found: ' + input_json)

    if not db_name.endswith('.db'):
        raise Exception('DB name must end with .db')

    conn = sqlite3.connect(db_name)

    c = conn.cursor()

    querystr = """CREATE TABLE """ + tablename + """ (
        id integer primary key autoincrement,
        name text not null,
        isinstance integer not null,
        childof integer not null,
        childcount integer not null,
        instancecount integer not null,
        mentioncount integer not null
        )"""

    c.execute(querystr)

    with open(input_json) as jsonFile:
        rootnode = json.load(jsonFile)
        parse_node(node=rootnode, cursor=c, tablename=tablename, is_instance=False, child_of=None, level=0)

    conn.commit()

    conn.close()


def argument_parser():
    # define argument menu
    description = "Creates a SQLite DB database file from a StoryTeller JSON file"
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-i', '--input', default='', help='Input JSON file', type=str, required=True)
    parser.add_argument('-n', '--name', default='', help='DB name (must end with .db)', type=str, required=True)
    parser.add_argument('-t', '--tablename', default='', help='table name', type=str, required=True)
    return parser


def main():
    try:
        a = argument_parser().parse_args()
        run(a.input, a.name, a.tablename)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
