import turtle
import time
wn = turtle.Screen()
wn.bgcolor("white")
snake = turtle.Turtle()
snake.color("darkgreen")
snake.pensize(5)
snake.speed(0)
snake.hideturtle()
snaketail = turtle.Turtle()
snaketail.color("white")
snaketail.pensize(5)
snaketail.speed(0)
snaketail.hideturtle()
speed = 1
oldx = 0
oldy = 0
oldoldx = 0
oldoldy = 0
turnedLeft = False
turnedRight = False
timer = 5

def addspeed():
    global speed
    speed = 2
def resetx():
    global x
    global oldx
    global oldoldx
    x = snake.xcor()
    oldoldx = oldx
    oldx = x 
def resety():
    global y
    global oldy
    global oldoldy
    y = snake.ycor()
    oldoldy = oldy
    oldy = y
def left():
    global turnedLeft
    snake.left(90)
    resetx()
    resety()
    turnedLeft = True

def right():
    global turnedRight
    snake.right(90)
    resetx()
    resety()
    turnedRight = True
turtle.listen()
turtle.onkey(left, "Left")
turtle.onkey(right, "Right")
while True:
    snake.forward(2)
    snaketail.forward(speed)
    x = snake.xcor()
    y = snake.ycor()
    if (snaketail.xcor() == oldx) and (snaketail.ycor() == oldy):
        if turnedLeft == True:
            snaketail.left(90)
            addspeed()
            turnedLeft = False
        if turnedRight == True:
            snaketail.right(90)
            addspeed()
            turnedRight = False
    if (snaketail.xcor() == oldoldx) and (snaketail.ycor() == oldoldy):
        if turnedLeft == True:
            snaketail.left(90)
            addspeed()
            turnedLeft = False
        if turnedRight == True:
            snaketail.right(90)
            addspeed()
            turnedRight = False


#-------------------------------------debug code-------------------------------
#print("oldx", oldx)
#print("oldy", oldy)
#print(x)
#print(y)
#print("tailx", snaketail.xcor())
#print("taily", snaketail.ycor())
#print("oldoldx", oldoldx)
#print("oldoldy", oldoldy)
#print("\n")


