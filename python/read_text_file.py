#!/usr/bin/python3

# [https://stackoverflow.com/questions/3277503/how-to-read-a-file-line-by-line-into-a-list]
# [https://stackoverflow.com/questions/8369219/how-to-read-a-text-file-into-a-string-variable-and-strip-newlines]


import os
import sys


if __name__ == '__main__':

    FILENAME = sys.argv[1]

    #
    with open(FILENAME) as file:
        lines = [line.rstrip() for line in file]

    print(f'{os.linesep}---[ readlines ]---{"---"*20}{os.linesep}')
    for line in lines:
        print(line)

    #
    with open(FILENAME) as file:
        single_str = file.read()

    print(f'{os.linesep}---[ bulk ]---{"---"*21}{os.linesep}')
    print(single_str)
