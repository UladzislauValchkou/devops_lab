#!/bin/python
#pylint:disable=invalid-name
""" task 1 """
N = int(input("Enter integer number: "))
for i in range(N):
    if i < N:
        print(i * i)
    else:
        break
