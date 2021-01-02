#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def isprime(n):
    if n <= 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True

n = int(input("enter number: " ))

x = [] # to create a list out from calling a function

def list_primes():
    for i in range (n+1):
        if isprime(i):
            x.append(i)
            print(i, end= " ", flush=True)

    print()


list_primes()

print (x)


n = 5
if isprime(n):
    print(f'{n} is prime')
else:
    print(f'{n} not prime')



