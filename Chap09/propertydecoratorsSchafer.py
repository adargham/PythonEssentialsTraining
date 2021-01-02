#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class Employee:

    num_of_emps = 0                # class variables should be the same for all instances
    raise_amt =  1.04

    def __init__(self, first, last, pay):
        self.first = first                        # each is an instance variable whereas
        self.last  = last
        self.pay = pay

    @property
    def email(self):
        return f'{self.first.lower()}@{self.last.lower()}.ch'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

emp_1 = Employee('Alain','Dargham',60000)
emp_2 = Employee('Mark', 'Dargham', 70000)


# print(emp_1.email())  changed by adding property
print(emp_1.first)
print(emp_2.email)
print(emp_2.fullname)
