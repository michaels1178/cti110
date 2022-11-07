#This program dtaws my initials using turtle graphics
#November 6, 2022
#CTI-110 P4LAB1b: Initials
#Michael A. Simmons
#
# There is a setup to draw the letter "M" the first initial of my name
# There is a setup to draw the letter "S" the second initial of my name
# The program keeps the window open until loop closes

#initialize
import turtle
  
#setting up workscreen
win=turtle.Screen()
  
#defining turtle instance
t=turtle.Turtle()
turtle.Screen().bgcolor("red")
t.pensize(8)
t.color("yellow")
  
#for printing letter "M"
t.right(90)
t.forward(150)
t.backward(150)

t.left(45)
t.forward(90)

t.left(95)
t.forward(90)

t.right(140)
t.forward(150)

#for printing letter "S"
t.penup()
t.setpos(245,-5)
t.pendown()

t.right(100)
t.forward(10)

t.circle(35,185)
t.circle(-45,185)
t.penup()

win.mainloop()
