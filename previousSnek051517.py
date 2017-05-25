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
snaketailcopy = turtle.Turtle()
snaketail.color("blue")
snaketail.pensize(5)
snaketail.speed(0)
snaketail.hideturtle()
coords = []
copycoords = []
count = 0
turns = 0
speed = 2
apple = 0
tailspeed = 1
turnedLeft = False
turnedRight = False
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
def left():
    global turnedLeft
    global turns
    turns += 1
    snake.left(90)
    resetcoords()
    turnedLeft = True
    global apple
    apple = 1
def right():
    global turnedRight
    global turns
    turns += 1
    snake.right(90)
    resetcoords()
    turnedRight = True
    global apple
    apple = 1
turtle.listen()
turtle.onkey(left, "Left")
turtle.onkey(right, "Right")
while True:
    snake.forward(speed)
    snaketail.forward(tailspeed)
    snaketailcopy.forward(0.5)
##    print(speed)
##    print("tail", tailspeed)
##    print("turns", turns)
##    print("coords list", coords)
##    print("snake coords", snake.xcor(), snake.ycor()) 
##    print("snaketail coords", snaketail.xcor(), snaketail.ycor())
##    print("\n")
##    print(copycoords)
    x = snake.xcor()
    y = snake.ycor()
    x2 = snaketailcopy.xcor()
    y2 = snaketailcopy.ycor()
    count += 1
    for x in range(turns):
        if (snaketail.xcor() == coords[x][0]) and (snaketail.ycor() == coords[x][1]):
            if turnedLeft == True:
                snaketail.left(90)
                addspeed()
                tailspeed = speed
                turnedLeft = False
            if turnedRight == True:
                snaketail.right(90)
                addspeed()
                tailspeed = speed
                turnedRight = False
        if (apple == 1):
                oldspeed = speed
                speed = oldspeed + 0.5
                apple = 0
    for x in range(count):
        copycoords.append([])
        copycoords[count - 1].append(x2)
        copycoords[count - 1].append(y2)
        

#-------------------------------------debug code-------------------------------
##    print("turns", turns)
##    print("coords list", coords)
##    print("snake coords", snake.xcor(), snake.ycor()) 
##    print("snaketail coords", snaketail.xcor(), snaketail.ycor())
##    print("\n")

