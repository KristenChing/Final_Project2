import turtle
import time
from turtle import *
setup(560, 585)
wn = turtle.Screen()
wn.bgcolor("white")
wn.title("turtle.py")
wn.bgpic("maze-easy.gif")
pen = turtle.Turtle()
pen.penup()
pen.hideturtle()
pen.speed(0)
pen.goto(-400,0)
pen.write("hello", font = ("Arial", 90, 'normal'))
time.sleep(1)
pen.clear()
pen.forward(300)
pen.write("welcome", font = ("Arial", 90, 'normal'))
time.sleep(1)
pen.clear()
pen.goto(450, 350)
pen.hideturtle()
            
move = Turtle(shape = "turtle")
move.hideturtle()
move.penup()
move.goto(-250, 250)
move.showturtle()

def boundary_check():
    move.speed(0)
    if move.xcor() > 250 or move.xcor() < -250: 
        move.right(180)
    if move.ycor() > 250 or move.ycor() < -250:
        move.right(180)

def forward():
    move.forward(30)
    boundary_check()

def left():
    move.left(90)
    boundary_check()

def right():
    move.right(90)
    boundary_check()

wn.onkeypress(forward, "Up")
wn.onkeypress(left, "Left")
wn.onkeypress(right, "Right")
wn.listen()
wn.mainloop()
