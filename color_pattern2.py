import turtle
import random

colors =["#ff0000", "#d61a1a","#a50000","#ddb200","#e7e497"]

for i in range(len(colors)+1):
    colors = colors+colors

pen = turtle.Turtle()
pen.shape("classic")
size = 20;

x,y= -80, 80
count = 0
for i in range(6):
    pen.penup()
    for j in range(6):
        pen.penup()
        pen.goto(x,y)
        pen.down()
        pen.fillcolor(colors[count])
        count +=1
        pen.begin_fill()
        pen.circle(size)
        pen.end_fill()
        pen.penup()
        x = x+40

    x = -80
    y = y-40


pen.penup()


turtle.exitonclick()
