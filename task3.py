#!/bin/python
#pylint:disable=invalid-name
""" task 3 """
canvas_size = str(input('input height and width of the canvas ')).split()
a = int(canvas_size[0])
b = int(canvas_size[1])
canvas_square = a * b
rectangle_quantity = int(input("input rectangles quantity "))
while rectangle_quantity > 0:
    rectangle_size = str(input("input h and w of the rectangle ")).split()
    c = int(rectangle_size[0])
    d = int(rectangle_size[1])
    rectangle_square = c * d
    canvas_square = canvas_square - rectangle_square
    rectangle_quantity -= 1
print(canvas_square)
