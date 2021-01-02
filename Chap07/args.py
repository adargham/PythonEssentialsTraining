#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    kitten('meow', 'grrr', 'purr')

def kitten(*args):
    if len(args):     # remember 0 is False i.e. if else statement works
        for s in args:
            print(s)
    else: print('No Args.')

if __name__ == '__main__': main()


def main():
    kitten()

def kitten(*args):
    if len(args):     # remember 0 is False i.e. if else statement works
        for s in args:
            print(s)
    else: print('No Args!')

if __name__ == '__main__': main()


def main():
    x = ('meow', 'grrr', 'purr','Hello', 'World')
    kitten(*x)
    print(x)


def kitten(*args):
    if len(args):     # remember 0 is False i.e. if else statement works
        for s in args:
            print(s)
    else: print('No Args.')

if __name__ == '__main__': main()

