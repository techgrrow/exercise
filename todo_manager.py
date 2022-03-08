# -*- coding: utf-8 -*-

import argparse


parser = argparse.ArgumentParser()

parser.add_argument("h", help="show all available actions")
parser.add_argument("ls", help="show all todos sorted by added date desc.")
parser.add_argument("a", help="add todo (params: title)")
parser.add_argument("e",  help="edit todo (params: id, title)")
parser.add_argument("d", help="delete todo (params: id, title)")
parser.add_argument("t", help="toggle done state: True/False (params: id, title)")
parser.add_argument("s", help="search todo titles for inserted string (params: <search string>)")

args = parser.parse_args()



if __name__ == '__main__':

    if args.h:
        pass

    if args.ls:
        pass

    if args.a:
        pass

    if args.e:
        pass

    if args.d:
        pass

    if args.t:
        pass

    if args.s:
        pass

