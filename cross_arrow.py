import turtle


pen = turtle.Turtle()
pen.shape("arrow")
pen.color("red")

pen.penup()
pen.goto(0,-180)
pen.pendown()
pen.goto(0,180)

pen.penup()
pen.goto(-180,0)
pen.pendown()
pen.goto(180,0)

turtle.mainloop()
