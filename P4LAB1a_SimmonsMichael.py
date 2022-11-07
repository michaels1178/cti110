#This program creates shape using turtle graphics
#November 6, 2022
#CTI-110 P4LAB1a: Shapes
#Michael A. Simmons
#
# There is a setup to draw a square as the first turtle object
# There is a setup to draw a triangle as the second turtle object
# To draw a square the program should repeat 4 times
# To draw a triangle the program should repeat 3 times
# The program keeps the window open until loop closes

#initialize
import turtle
win = turtle.Screen()
win.bgcolor("lightgreen")

s = turtle.Screen()
square = turtle.Turtle()
square.pensize(8)
square.color("red")

triangle = turtle.Turtle()
triangle.pensize(8)
triangle.color("blue")

user_num = 0
while user_num < 4:
    square.forward(150)
    square.left(90)
    user_num = user_num + 1

#for printing letter "triangle"
    triangle.penup()
    triangle.setpos(220,-0)
    triangle.pendown()

user_num = 0
while user_num < 3:
    triangle.forward(150)
    triangle.left(120)
    user_num = user_num + 1

win.mainloop()
