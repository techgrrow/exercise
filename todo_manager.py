# -*- coding: utf-8 -*-

import argparse
import os
import calendar
import time

todo_list = []
todo_present = False
todo_db = "todo.db"  # db file path

# adding arguments
parser = argparse.ArgumentParser()

parser.add_argument("-ls", "--list", dest="list", action='store_true', help="show all todos sorted by added date desc.")
parser.add_argument("-a", "--add", dest="add", help="add todo (params: title)")
parser.add_argument("-e", "--edit", nargs='+', dest="edit", help="edit todo (params: id, title)")
parser.add_argument("-d", "--delete", dest="delete", help="delete todo (params: id, title)")
parser.add_argument("-t", "--toggle", dest="toggle", help="toggle done state: True/False (params: id, title)")
parser.add_argument("-s", "--search", dest="search", help="search todo titles for inserted string "
                                                          "(params: <search string>)")
"""
the -h/---help argument is already present in this library
#parser.add_argument("-h", "--help", help="show all available actions") 
"""
args = parser.parse_args()


def check_no_todo():
    global todo_list, todo_db, todo_present
    try:
        todo_present = False if os.stat(todo_db).st_size == 0 else True
    except:
        open(todo_db, 'w')  # creates file if not present


def load_todos():
    global todo_list, todo_db
    try:
        with open(todo_db, 'r') as file:
            file_content = file.read()
            todo_list = list(eval(file_content))
    except Exception as e:
        print('Error loading db file: ', e)


def get_timestamp():
    current_gmt = time.gmtime()
    ts = calendar.timegm(current_gmt)
    return ts


def write_to_file(content):
    global todo_db
    try:
        with open(todo_db, 'w') as file:
            file.write(str(content))
    except Exception as e:
        print('Error loading db file: ', e)


def validate_id(note_id):
    if todo_present:
        try:
            if note_id.isnumeric() and int(note_id) <= len(todo_list):
                return int(note_id)
        except Exception as e:
            print('Error with todo id inserted: ', e)
    else:
        print("No todo inserted yet. Add a new Todo.")


if __name__ == '__main__':

    check_no_todo()
    if todo_present:
        load_todos()

    if args.list:
        if os.stat(todo_db).st_size == 0:
            print('No todos added yet')
        else:
            print(todo_list)

    if args.add:
        todo = {'id': len(todo_list) + 1,
                'title': args.add,
                'done': False,
                'timestamp': get_timestamp()}
        todo_list.append(todo)
        write_to_file(todo_list)

    if args.edit:
        todo_id = validate_id(args.edit[0])
        if todo_present and todo_id:
            title = args.edit[1]
            if len(title) > 4:
                todo_list[todo_id - 1]['title'] = title
                write_to_file(todo_list)
            else:
                print('Title must be 5 or more characters')
        else:
            print("No todo to edit or ID not valid.")

    if args.delete:
        pass

    if args.toggle:
        pass

    if args.search:
        pass
