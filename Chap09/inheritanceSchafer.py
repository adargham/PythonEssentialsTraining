#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/



class Employee:

    num_of_emps = 0                # class variables should be the same for all instances
    raise_amt =  1.04

    def __init__(self, first, last, pay):
        self.first = first                        # each is an instance variable whereas
        self.last  = last
        self.pay = pay
        self.email = first.lower() + '@'+ last.lower() +'.ch'

        Employee.num_of_emps += 1         # here we did not use the self because this is a constant that must not change between an employee and another

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)   # we can use Emplyee.raise_amount instead but this gives the flexilibity to change a signle instance

class Developer (Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager (Employee):

    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('- - - >', emp.fullname())


dev_1 = Developer('Alain','Dargham',60000, 'Python')
dev_2 = Developer('Mark', 'Dargham', 70000, 'C')
mgr_1 = Manager('Sue','Smith',90000, employees = [dev_1])

print(mgr_1.email)

mgr_1.add_emp(dev_2)
mgr_1.remove_emp((dev_1))

mgr_1.print_emps()

print(isinstance(mgr_1,Manager))
print(isinstance(mgr_1, Employee))

print(isinstance(mgr_1, Developer))

print(issubclass(Manager, Employee))
print(issubclass(Manager, Developer))



