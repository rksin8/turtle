import turtle
import random

colors =["#FF0000","#FFA600","#FFFF00", "#62FF00", "#1E56FC","#4800FF","#CC00FF","#69C5FF"]
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
        color = random.choice(colors)
        pen.fillcolor(color)
        pen.begin_fill()
        pen.circle(size)
        pen.end_fill()
        pen.penup()
        x = x+40

    x = -80
    y = y-40


pen.penup()

turtle.exitonclick()
