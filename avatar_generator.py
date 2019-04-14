import turtle
import random

pen = turtle.Turtle()
pen.shape("turtle")
pen.speed(500)

window = turtle.Screen()
window.bgcolor("#69C5FF")

skinColors = ["#FCD09D","#FAC47A", "#DBA965", "#CC9D5E","#A3855B","#806645","#665135"]
eyeColors = ["#489CF0","#15A315", "#8C3303"]
hairColors = ["#000000","#8C3303","#F5D907","#580000","#E31E00","#636363","#FFFFFF"]

pen.penup()
pen.goto(0,-100)

#skinColorIndex=int(input("Chose a skin complexion from 1 (pale) to 7 (dark skin)?"))-1
#eyeColorIndex=int(input("Color of the eyes? Chose between 1 - blue, 2 - green, 3 - brown."))-1
#hairColorIndex=int(input("Hair color? Chose between 1 - black, 2 - brown, 3 - Blond, 4 - Auburn, 5 - Red, 6 - Grey, 7 - White."))-1

skinColorIndex = random.randint(0,6)
eyeColorIndex = random.randint(0,2)
hairColorIndex = random.randint(0,6)

def drawHair():
  #Drawing the hair
  pen.penup()
  pen.goto(-50,-50)
  pen.pendown()
  pen.color(hairColors[hairColorIndex])
  pen.fillcolor(hairColors[hairColorIndex])
  pen.begin_fill()
  pen.goto(-160,20+random.randint(-10,10))
  pen.goto(-140,110+random.randint(-10,10))
  pen.goto(-130,100+random.randint(-10,10))
  pen.goto(-110,160+random.randint(-10,10))
  pen.goto(-90,150+random.randint(-10,10))
  pen.goto(-70,180+random.randint(-10,10))
  pen.goto(-50,160+random.randint(-10,10))
  pen.goto(-40,190+random.randint(-10,10))
  pen.goto(-10,160+random.randint(-10,10))
  pen.goto(20,180+random.randint(-10,10))
  pen.goto(50,160+random.randint(-10,10))
  pen.goto(70,150+random.randint(-10,10))
  pen.goto(90,160+random.randint(-10,10))
  pen.goto(110,140+random.randint(-10,10))
  pen.goto(130,170+random.randint(-10,10))
  pen.goto(140,110+random.randint(-10,10))
  pen.goto(160,20+random.randint(-10,10))
  pen.goto(-50,-50)
  pen.end_fill()

def drawFace():
  #Drawing the face
  pen.penup()
  pen.goto(0,-150)
  pen.color(skinColors[skinColorIndex])
  pen.fillcolor(skinColors[skinColorIndex])
  pen.begin_fill()
  pen.circle(150)
  pen.end_fill()

def drawSmile():
  #Drawing the smile
  pen.penup()
  pen.goto(0,-100)
  pen.color("#F00070")
  pen.fillcolor("#F00070")
  pen.begin_fill()
  pen.circle(70)
  pen.end_fill()  

  pen.penup()
  pen.goto(0,-85)
  pen.color(skinColors[skinColorIndex])
  pen.fillcolor(skinColors[skinColorIndex])
  pen.begin_fill()
  pen.circle(80)
  pen.end_fill()

def drawEyeBrow(x):
  #Drawing one eyeBrow at position x
  pen.penup()
  pen.goto(x,50)
  pen.color(hairColors[hairColorIndex])
  pen.fillcolor(hairColors[hairColorIndex])
  pen.begin_fill()
  pen.circle(30)
  pen.end_fill()

  pen.penup()
  pen.goto(x,20)
  pen.color(skinColors[skinColorIndex])
  pen.fillcolor(skinColors[skinColorIndex])
  pen.begin_fill()
  pen.circle(40)
  pen.end_fill()

def drawEye(x):
  #Drawing one eyeBrow at position x
  pen.penup()
  pen.goto(x,20)
  pen.color("#000000")
  pen.fillcolor("#FFFFFF")
  pen.begin_fill()
  pen.circle(30)
  pen.end_fill()

  pen.penup()
  pen.goto(x,30)
  pen.color(eyeColors[eyeColorIndex])
  pen.fillcolor(eyeColors[eyeColorIndex])
  pen.begin_fill()
  pen.circle(20)
  pen.end_fill()

  pen.penup()
  pen.goto(x,40)
  pen.color("#000000")
  pen.fillcolor("#000000")
  pen.begin_fill()
  pen.circle(10)
  pen.end_fill()

drawHair()
drawFace()
drawSmile()
drawEyeBrow(-60)
drawEyeBrow(60)
drawEye(-60)
drawEye(60)




pen.penup()
pen.goto(200,240)

turtle.exitonclick()
