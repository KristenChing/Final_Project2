import turtle
import time
import random
wn = turtle.Screen()
wn.bgcolor("white")
apeat= 0
apple = turtle.Turtle()
apple.penup()
apple.shape("turtle")
apple.fillcolor("red")
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
w = 0
z = 0
coords = []
leftRightTurns = []
turns = 0
speed = 2
tailspeed = 1
ateApple = False
turnedLeft = False
turnedRight = False
lastTurn = ""
leftTurns = 0
rightTurns = 0
timer = 5
def addspeed():
    global tailspeed
    tailspeed = 2
def resetcoords():
    global x
    x = snake.xcor()
    global y
    y = snake.ycor()
    coords.append([])
    coords[turns - 1].append(x)
    coords[turns - 1].append(y)
def addLeft():
    leftRightTurns[turns - 1].append("left")
def resetcOrds():
    global apeat
    apeat+=1
    ateApple = True
    apple.hideturtle()
    global w
    w = apple.xcor()
    global z
    z = apple.ycor()
    apple.goto(random.randint(-400, 400), random.randint(-400, 400))
    apple.showturtle()
resetcOrds()  

def left():
    print("snek turned left")
    global turnedLeft
    global turns
    global leftTurns
    global lastTurn
    turns += 1
    snake.left(90)
    resetcoords()
    turnedLeft = True
    leftTurns += 1
    print("left funct", turnedLeft)
    if turnedRight == True or rightTurns > 0:
        lastTurn = "right"
def right():
    print("snek turned right")
    global turnedRight
    global turns
    global rightTurns
    global lastTurn
    turns += 1
    snake.right(90)
    resetcoords()
    turnedRight = True
    rightTurns += 1
    print("right funct", turnedRight)
    if turnedLeft == True or leftTurns > 0:
        lastTurn = "left"
turtle.listen()
turtle.onkey(left, "Left")
turtle.onkey(right, "Right")
def followLeft():
    global leftTurns
    global tailspeed
    global turnedLeft
    snaketail.left(90)
    addspeed()
    tailspeed = speed
    turnedLeft = False
    leftTurns -= 1
    print("left")
def followRight():
    global rightTurns
    global tailspeed
    global turnedRight
    snaketail.right(90)
    addspeed()
    tailspeed = speed
    turnedRight = False
    rightTurns -= 1
    print("right")
while True:
    snake.forward(speed)
    snaketail.forward(tailspeed)
##    print(speed)
##    print("tail", tailspeed)
##    print("turns", turns)
##    print("coords list", coords)
##    print("snake coords", snake.xcor(), snake.ycor()) 
##    print("snaketail coords", snaketail.xcor(), snaketail.ycor())
##    print("apple coords", apple.xcor(), apple.ycor()) 
##    print("\n")
    x = snake.xcor()
    y = snake.ycor()
    w = apple.xcor()
    z = apple.ycor()
    for x in range(turns):
        #print(x)
        if (snaketail.xcor() == coords[x][0]) and (snaketail.ycor() == coords[x][1]):
            print("ran")
            print("turnedLeft", turnedLeft)
            print("turnedRight", turnedRight)
            print("left turns", leftTurns)
            print("right turns", rightTurns)
            print("lastTurn", lastTurn)
            if lastTurn == "right":
                followRight()
                lastTurn = ""
            if lastTurn == "left":
                followLeft()
                lastTurn = ""
            else:
                if (turnedLeft == True) or (leftTurns > 0):
                    followLeft()
                if (turnedRight == True) or (rightTurns > 0):
                    followRight()
    for i in range (int(w) - 10, int(w) + 10):
        #print("w", w)
        #print("i", i)
        if (i > snake.xcor() - 10) and (i < snake.xcor() + 10):
            for j in range (int(z) - 5, int(z) + 5):
                #print("j", j)
                if (j > snake.ycor() - 5) and (j < snake.ycor() + 5):
                    resetcOrds()
        if ateApple == True:
                oldspeed = speed
                speed = oldspeed + 0.5
                ateApple = False                                 

apple.listen()

#-------------------------------------debug code-------------------------------
##    print("turns", turns)
##    print("coords list", coords)
##    print("snake coords", snake.xcor(), snake.ycor()) 
##    print("snaketail coords", snaketail.xcor(), snaketail.ycor())
##    print("\n")
