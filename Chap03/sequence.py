#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/


x = [ 1, 2, 3, 4, 5 ]
for i in x:
    print(f'is is {i}')
print('\n')


x = [ 1, 2, 3, 4, 5 ]
x[3] = 42
for i in x:
    print('i is {}'.format(i))
print('\n')


# x = ( 1, 2, 3, 4, 5 )
# x[3] = 42
# for i in x:
    # print('i is {}'.format(i))

x = ( 1, 2, 3, 4, 5 )
for i in x:
    print('i is {}'.format(i))
print('\n')


# we can create a sequence using range
y = []
x = range(5+1)
for i in x:
    y.append(i)
    print('i is {}'.format(i))
print(y)
print('\n')

# to create an immutabale range
x = list(range(5+1))
for i in x:
    print('i is {}'.format(i))
print(x)
print('\n')

x = list(range(5+1))
x[3] = 42
for i in x:
    print('i is {}'.format(i))
print(x)
print('\n')

# x = range(5+1)
# x[3] = 42
# for i in x:
    # print('i is {}'.format(i))
# print(x)
# print('\n')

# Dictinary

x = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
for k,v in x.items():
    print(f' k: {k}, v: {v} ')

print (x)
print('\n')


x = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
x['three'] = 42
for k,v in x.items():
    print(f' k: {k}, v: {v} ')

print (x)
print('\n')