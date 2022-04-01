#!/usr/bin/python3

# [https://stackoverflow.com/questions/5574702/how-to-print-to-stderr-in-python#14981125]


import sys


if __name__ == '__main__':

    if len(sys.argv) < 4:
        print('*** Usage:', file=sys.stderr)
        print(f'    {sys.argv[0]}   arg1   arg2   arg3   [arg4   [...]]', file=sys.stderr)
        print(file=sys.stderr)
        sys.exit(1)

    ARG1 = sys.argv[1]
    ARG2 = sys.argv[2]
    ARG3 = sys.argv[3]

    print(f'ARG1 = {ARG1}')
    print(f'ARG2 = {ARG2}')
    print(f'ARG3 = {ARG3}')
