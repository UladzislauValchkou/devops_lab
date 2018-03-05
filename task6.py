#!/bin/python
#pylint:disable=invalid-name
""" task 6 """
sentence = str(input("Enter your sentence: ")).split()
x = len(sentence)
for i in range(x):
    sentence[i] = sentence[i][::-1]
print(" ".join(sentence))
