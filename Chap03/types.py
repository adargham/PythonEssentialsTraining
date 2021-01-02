#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = 7
print('x is {}'.format(x))
print(type(x))

x = 7.0
print(f'x is {x}')
print(type(x))

x = "7.0"
print('x is {}'.format(x))
print(type(x))

x = True
print('x is {}'.format(x))
print(type(x))

x = None
print('x is {}'.format(x))
print(type(x))

x = "seven"
print('x is {}'.format(x))
print(type(x))

x = 'seven'.capitalize()
print('x is {}'.format(x))
print(type(x))

x = 'seven'.upper()
print('x is {}'.format(x))
print(type(x))

x = 'seven'.lower()
print('x is {}'.format(x))
print(type(x))

x = 'seven {} {}'.format(8,9)
print('x is {}'.format(x))
print(type(x))


x = 'seven {1} {0}'.format(8,9) # change position using indexing
print('x is {}'.format(x))
print(type(x))

x = 'seven {1:<9} {0:>9}'.format(8,9) # left and right align using spaces
print('x is {}'.format(x))
print(type(x))


x = 'seven "{1:<09}" "{0:>09}"'.format(8,9) # left and right align using spaces
print('x is {}'.format(x))
print(type(x))

a = 8
b = 9
x = f'seven {a} {b}'
print('x is {}'.format(x))
print(type(x))

a = 8
b = 9
x = f'seven {a:<09} {b:>09}'
print('x is {}'.format(x))
print(type(x))


# Numeric Types

x = 7
print('x is {}'.format(x))
print(type(x))

x = 7 / 3
print('x is {}'.format(x))
print(type(x))


x = 7 // 3
print('x is {}'.format(x))
print(type(x))

x = 7 % 3
print('x is {}'.format(x))
print(type(x))

x = .1 + .1 + .1 - .3  # scarifying accuracy for precision 17 decimal places. it is not accurate
print('x is {}'.format(x))
print(type(x))

from decimal import *

a = Decimal(".10")
b = Decimal(".30")
x = a + a + a - b
print('x is {}'.format(x))
print(type(x))


# Bool types

x = 7
print('x is {}'.format(x))
print(type(x))

x = 7 > 5
print('x is {}'.format(x))
print(type(x))

x = None
print('x is {}'.format(x))
print(type(x))


x = None
print('x is {}'.format(x))
print(type(x))
if x :
     print ("True")
else:
    print ("False")


x = None
print('x is {}'.format(x))
print(type(x))
if x :
     print ("True")
else:
    print ("False")



x = 0
print('x is {}'.format(x))
print(type(x))
if x :
     print ("True")
else:
    print ("False")

x = ''
print('x is {}'.format(x))
print(type(x))
if x :
     print ("True")
else:
    print ("False")

x = 'n'
print('x is {}'.format(x))
print(type(x))
if x :
     print ("True")
else:
    print ("False")

# Tuples

x = (1, 2, 3, 4, 5)
print(x)
print(type(x))


x = (1, 'two', 3.0, 4, 'four', 5)
y = (2, 'two', 3.0, 4, 'four', 5)
print(x)
print(type(x))
print(type(y))
print(type(x[1]))

print(id(x))
print(id(y))

print(id(x[1]))
print(id(y[1]))