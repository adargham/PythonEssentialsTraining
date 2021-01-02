#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

print('Hello, World.')

def f1():
    print ('this is f1')

x = f1
x()



def f1():  #Ç f1 is wrapper to f2
    def f2():
        print ('this is f2')
    return f2()

x = f1
x()   # f2 cannot be called directly


def f1(f):  #Ç f1 is wrapper to f2
    def f2():
        print ('this is before the function call')
        f()
        print('this is after the function call')
    return f2()

def f3():
    print('This is f3')

y = f1(f3)
y()