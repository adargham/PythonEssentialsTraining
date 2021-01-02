#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

a = True
b = False
x = ( 'bear', 'bunny', 'tree', 'sky', 'rain' )
y = 'bear'

if a and b:
    print('expression is true')
else:
    print('expression is false')


if b:
    print('yes')
else:
    print('nope')



if y in x:
    print('expression is true')
else:
    print('expression is false')

if y in x[0]:
    print('expression is true')
else:
    print('expression is false')

print(id(y))
print(id(x[0]))

z = len(str(id(x)))
print(z)
