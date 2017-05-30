import turtle
import time
import random
turtel = turtle.Turtle()
turtel.penup()
turtel.goto(0, 370)
wn = turtle.Screen()
wn.bgcolor("white")
mypen = turtle.Turtle()
mypen.color("black")
mypen.penup()
mypen.setposition(-360,-390)
mypen.pendown()
mypen.pensize(3)
for side in range(4):
    mypen.forward(750)
    mypen.left(90)
mypen.hideturtle()
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
snaketail.color("blue")
snaketail.pensize(10)
snaketail.speed(0)
snaketail.hideturtle()
w = 0
z = 0
coords = []
leftRightTurns = []
turns = 0
speed = 1
tailspeed = 0
ateApple = False
applereset = 0
gamestart = True
followed = False
def addspeed():
    global tailspeed
    tailspeed = 1
def resetcoords():
    global x
    x = snake.xcor()
    global y
    y = snake.ycor()
    coords.append([])
    coords[turns - 1].append(x)
    coords[turns - 1].append(y)
def addLeft():
    leftRightTurns.append("left")
def addRight():
    leftRightTurns.append("right")
def resetcOrds():
    global ateApple
    global applereset
    applereset += 1
    if gamestart == True:
        print("")
    else:
        ateApple = True
    apple.hideturtle()
    global w
    w = apple.xcor()
    global z
    z = apple.ycor()
    apple.goto(random.randint(-350, 350), random.randint(-350, 350))
    apple.showturtle()
resetcOrds()
gamestart = False
applereset = 0
def boundary_check_snake():
    if snake.xcor() > 360 or snake.xcor() < -360:
        mypen.penup()
        mypen.goto(-150,0)
        mypen.write("you died", font = ("Arial", 90, 'normal'))
        while True == True:
            snake.forward(0)
    if snake.ycor() > 370 or snake.ycor() < -370:
        mypen.penup()
        mypen.goto(-150,0)
        mypen.write("you died", font = ("arial", 90, 'normal'))
        while True == True:
            snake.forward(0)        
def left():
    print("snek turned left")
    global turns
    global tailspeed
    global gamestart
    global followed
    if gamestart == True:
        addspeed()
        gamestart = False
    else:
        tailspeed = speed
    followed = False
    turns += 1
    print(turns)
    snake.left(90)
    resetcoords()
    addLeft()
def right():
    print("snek turned right")
    global turns
    global tailspeed
    global gamestart
    global followed
    if gamestart == True:
        addspeed()
        gamestart = False
    else:
        tailspeed = speed
    followed = False
    turns += 1
    print(turns)
    snake.right(90)
    resetcoords()
    addRight()
turtle.listen()
turtle.onkey(left, "Left")
turtle.onkey(right, "Right")
def followLeft():
    global tailspeed
    snaketail.left(90)
    print("left")
def followRight():
    global tailspeed
    snaketail.right(90)
    print("right")
while True:
    snake.forward(speed)
    snaketail.forward(tailspeed)
    boundary_check_snake()
    print(speed)
    print("tail", tailspeed)
    #print("turns", turns)
    print("coords list", coords)
    print("snake coords", snake.xcor(), snake.ycor()) 
    print("snaketail coords", snaketail.xcor(), snaketail.ycor())
    #print("apple coords", apple.xcor(), apple.ycor())
    print("leftRightTurns", leftRightTurns)
    print("\n")
    x = snake.xcor()
    y = snake.ycor()
    w = apple.xcor()
    z = apple.ycor()
    for x in range(turns):
        #print("x", x)
        print(followed)
        if (snaketail.xcor() >= coords[x][0] - 2) and (snaketail.xcor() <= coords[x][0] + 2):
            if (snaketail.ycor() >= coords[x][1] - 2) and (snaketail.ycor() <= coords[x][1] + 2):    
                if followed == False:
                    print("ran")
                    if leftRightTurns[x] == "right":
                        tailspeed = speed
                        followRight()
                        followed = True
                    if leftRightTurns[x] == "left":
                        tailspeed = speed
                        followLeft()
                        followed = True
        #print("ar", applereset)
        #print("AA", ateApple)
    if applereset == 0:
        for i in range (int(w) - 5, int(w) + 5):
            #print(applereset)
            if (i > snake.xcor() - 5) and (i < snake.xcor() + 5):
                #print("i", i)
                #print(snake.xcor())
                for j in range (int(z) - 5, int(z) + 5):
                    if (j > snake.ycor() - 5) and (j < snake.ycor() + 5):
                        #print("j", j)
                        resetcOrds()
                        #print("apple reset", applereset)
    if ateApple == True:
            print("did i eat the apple")
            applereset = 0
            oldspeed = speed
            speed = oldspeed + 0.5
            tailspeed = speed
            ateApple = False                                 

apple.listen()

#-------------------------------------debug code-------------------------------
##    print("turns", turns)
##    print("coords list", coords)
##    print("snake coords", snake.xcor(), snake.ycor()) 
##    print("snaketail coords", snaketail.xcor(), snaketail.ycor())
##    print("\n")
