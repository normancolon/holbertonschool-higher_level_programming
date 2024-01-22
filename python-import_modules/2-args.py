#!/usr/bin/python3
import sys

if __name__ == '__main__':
    n = len(sys.argv) - 1
    print(f'{n} argument{'' if n == 1 else 's'}:')
    for i, arg in enumerate(sys.argv[1:], 1):
        print(f'{i}: {arg}')
