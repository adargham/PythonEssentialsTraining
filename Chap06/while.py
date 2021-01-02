#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

secret = 'swordfish'
pw = ''

auth = False
count = 0
max_attempt = 5

while pw != secret:
    count = count + 1
    if count > max_attempt: break
    pw = input(f'{count}: What is the secret word? ')
else:
    auth = True

if auth:
    print('Authorized!')
else:
    print('Calling the FBI !')

print('Authorized' if auth else 'Calling the FBI.....')