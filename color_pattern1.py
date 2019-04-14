import turtle
import random

colors =["#0099e6", "#43e0ef","#c3e970","#ffa9c2","#d297d9"]

pen = turtle.Turtle()
pen.shape("classic")
size = 20;

x,y= -80, 80
for i in range(len(colors)):
    pen.penup()
    for j in range(len(colors)):
        pen.penup()
        pen.goto(x,y)
        pen.down()
        pen.fillcolor(colors[j])
        pen.begin_fill()
        pen.circle(size)
        pen.end_fill()
        pen.penup()
        x = x+40

    x = -80
    y = y-40


pen.penup()


turtle.exitonclick()
