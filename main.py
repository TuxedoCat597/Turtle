import turtle
import random

#Change the background color to black
turtle.bgcolor("black")

#Adjust the speed of the turtle (lower = faster)
turtle.speed(0)

#List of colors
colors=["#1F0318","#B796AC","#4A5899","#559CAD","#7FB285"]

#Counter variables
color_num=0
size=1

#Change this variable to control how many sides your shape will have
sides=3

#Draw the spiraling shape
#This loops forever
while(True) :
  color_num=color_num+1
  for i in range(sides) :
    turtle.forward(size)
    turtle.right(360/sides + 1)
    size=size + 1
  turtle.color(colors[color_num%5])
  