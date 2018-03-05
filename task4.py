#!/bin/python
#pylint:disable=invalid-name
""" task 4 """
N = int(input("Enter integer number: "))
for a in range(N)[1:]:
    print("{:>{width}}{:>{width}}{:>{width}}{:>{width}}".format(int(a), oct(a)[2:], hex(a)[2:], bin(a)[2:], width=len(str(bin(N)[2:])) + 1))
