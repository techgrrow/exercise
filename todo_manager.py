# -*- coding: utf-8 -*-

import argparse
import os
import calendar
import time

todo_list = []
todo_db = "todo.db" #db file path

#adding arguments
parser = argparse.ArgumentParser()

parser.add_argument("-ls", "--list", dest="list", action='store_true', help="show all todos sorted by added date desc.")
parser.add_argument("-a", "--add", dest="add", help="add todo (params: title)")
parser.add_argument("-e", "--edit", dest="edit", help="edit todo (params: id, title)")
parser.add_argument("-d", "--delete", dest="delete", help="delete todo (params: id, title)")
parser.add_argument("-t", "--toggle", dest="toggle", help="toggle done state: True/False (params: id, title)")
parser.add_argument("-s", "--search", dest="search", help="search todo titles for inserted string "
                                                          "(params: <search string>)")
"""
the -h/---help argument is already present in this library
#parser.add_argument("-h", "--help", help="show all available actions") 
"""
args = parser.parse_args()



def load_todos():
    global todo_list, todo_db
    try:
        if os.stat(todo_db).st_size != 0:
            try:
                with open(todo_db, 'r') as file:
                    file_content = file.read()
                    todo_list = list(eval(file_content))
            except Exception as e:
                print('Error loading db file: ', e)
    except:
        open(todo_db, 'w') #creates file if not present



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


if __name__ == '__main__':

    load_todos()

    if args.list:
        if os.stat(todo_db).st_size == 0:
            print('No todos added yet')
        else:
            print(todo_list)

    if args.add:
        todo = {'id': len(todo_list),
                'title': args.add,
                'done': False,
                'timestamp': get_timestamp()}
        todo_list.append(todo)
        write_to_file(todo_list)

    if args.edit:
        pass

    if args.delete:
        pass

    if args.toggle:
        pass

    if args.search:
        pass

