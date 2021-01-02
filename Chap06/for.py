#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

animals = ('bear', 'bunny', 'dog', 'cat', 'velociraptor')

for pet in animals:
    print(pet)

for i in range(5):
    print(i)

x = list(range(5))
print(x)

for pet in animals:
    if pet == 'dog': continue
    if pet == 'velociraptor': break
    print(pet)
else:
    print('That is all!')

for pet in animals:
    if pet == 'dog': continue
    print(pet)
else:
    print('That is all!')
