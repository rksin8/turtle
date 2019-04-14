import turtle

pen = turtle.Turtle()
pen.shape("turtle")
pen.speed(5)

win = turtle.Screen()
win.bgcolor("#69C5FF")

rainbowColors = ["#FF0000","#FFA600","#FFFF00", "#62FF00", "#1E56FC","#4800FF","#CC00FF","#69C5FF"]

size = 180

pen.penup()
pen.goto(0,-360)

for color in rainbowColors:
    pen.color(color)
    pen.fillcolor(color)
    pen.begin_fill()
    pen.circle(size)
    pen.end_fill()
    size -=10

turtle.exitonclick()


