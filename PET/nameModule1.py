#!/usr/bin/env python3
# Copyright 2009-2020 https://www.youtube.com/watch?v=sugvnHA7ElY
# __Name__explained


def main():
    print(f'First module name: {__name__}')

if __name__ == '__main__':
    main()




print('This will always be run')
if __name__ == '__main__':
    print('Run directly')
else:
    print('Run from import')

