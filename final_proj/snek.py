import turtle
import time
import random
wn = turtle.Screen()
wn.bgcolor("black")
mypen = turtle.Turtle()
mypen.color("white")
mypen.penup()
mypen.hideturtle()
mypen.setposition(-270, 50)
mypen.write("Welcome to Snake", font = ("Arial", 50, 'normal'))
time.sleep(1)
mypen.setposition(-190, 0)
mypen.write("Made in Python Turtle", font = ("Arial", 30, 'normal'))
time.sleep(1)
mypen.setposition(-270, -50)
mypen.write("by Kristen Ching and Esther Choi", font = ("Arial", 30, 'normal'))
print("Loading...")
time.sleep(5)
print("start!")
mypen.clear()
wn.bgcolor("white")
mypen.color("black")
mypen.penup()
mypen.setposition(-360,-390)
mypen.pendown()
mypen.pensize(3)
for side in range(4):
    mypen.forward(750)
    mypen.left(90)
mypen.hideturtle()
mypen.penup()
mypen.setposition(-350, 370)
mypen.pendown()
apple = turtle.Turtle()
image = "apl.gif"
wn.addshape(image)
apple.shape(image)
apple.penup()
apple.turtlesize(1)
apple.fillcolor("red")
snake = turtle.Turtle()
snake.color("darkgreen")
snake.pensize(10)
snake.speed(0)
snake.hideturtle()
snaketail = turtle.Turtle()
snaketail.color("white")
snaketail.pensize(25)
snaketail.speed(0)
snaketail.hideturtle()
w = 0
z = 0
coords = []
leftRightTurns = []
tailTurns = 0
turns = 0
speed = 1
tailspeed = 0
scorestring = 0
score = 0
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
    if (snake.xcor() > 360 or snake.xcor() < -360) or (snake.ycor() > 370 or snake.ycor() < -370):
        mypen.penup()
        mypen.goto(-100,0)
        snake.clear()
        mypen.color("white")
        snaketail.clear()
        snaketail.hideturtle()
        snake.hideturtle()
        apple.hideturtle()
        wn.bgcolor("black")
        mypen.write("you died", font = ("Arial", 50, 'normal'))
        scorestring = "Final score: %s" %score
        mypen.color("white")
        mypen.goto(-100, -50)
        time.sleep(.5)
        mypen.write(scorestring, font=("Arial",30, "normal"))
        mypen.goto(-70, -90)
        time.sleep(.5)
        mypen.write("click to exit", font=("Arial",20, "normal"))
        for x in range(0, 9):
            mypen.clear()
            time.sleep(.1)
            mypen.write("click to exit", font=("Arial",30, "normal"))
        wn.exitonclick() 
def left():
    #print("snek turned left")
    global turns
    global tailspeed
    global gamestart
    global followed
    if gamestart == True:
        addspeed()
        gamestart = False
    else:
        tailspeed = speed
    #print(followed)
    followed = False
    #print(followed)
    turns += 1
    #print(turns)
    snake.left(90)
    resetcoords()
    addLeft()
def right():
    #print("snek turned right")
    global turns
    global tailspeed
    global gamestart
    global followed
    #print(followed)
    if gamestart == True:
        addspeed()
        gamestart = False
    else:
        tailspeed = speed
    #print(followed)
    followed = False
    turns += 1
    #print(turns)
    snake.right(90)
    resetcoords()
    addRight()
turtle.listen()
turtle.onkey(left, "Left")
turtle.onkey(right, "Right")
def followLeft():
    global tailspeed
    global tailTurns
    snaketail.left(90)
    #print("followed left")
    tailTurns += 1
def followRight():
    global tailspeed
    global tailTurns
    snaketail.right(90)
    #print("followed right")
    tailTurns += 1
while True:
    snake.forward(speed)
    snaketail.forward(tailspeed)
    boundary_check_snake()
    #print(speed)
    #print("tail", tailspeed)
##    print("turns", turns)
##    print("coords list", coords)
##    print("snake coords", snake.xcor(), snake.ycor()) 
##    print("snaketail coords", snaketail.xcor(), snaketail.ycor())
##    print("apple coords", apple.xcor(), apple.ycor())
##    print("leftRightTurns", leftRightTurns)
##    print("\n")
    x = snake.xcor()
    y = snake.ycor()
    w = apple.xcor()
    z = apple.ycor()
    for x in range(tailTurns, turns):
        #print("x", x)
        if (snaketail.xcor() >= coords[x][0] - 5) and (snaketail.xcor() <= coords[x][0] + 5):
            if (snaketail.ycor() >= coords[x][1] - 5) and (snaketail.ycor() <= coords[x][1] + 5):    
                if (followed == False) or (followed == True and turns > tailTurns):
                    #print("followed, 1", followed)
                    #print("turns", turns, "tailturns", tailTurns)
                    if leftRightTurns[x] == "right":
                        #print("ran right")
                        #print(followed)
                        tailspeed = speed
                        followRight()
                        followed = True
                    elif leftRightTurns[x] == "left":
                        #print("ran left")
                        tailspeed = speed
                        followLeft()
                        followed = True
                else:
                    snaketail.goto(coords[x][0], coords[x][1])
        #print("turns", turns)
        #print("tailturns", tailTurns)
        #print("coords list", coords)
        #print("snake coords", snake.xcor(), snake.ycor()) 
        #print("snaketail coords", snaketail.xcor(), snaketail.ycor())
        #print("leftRightTurns", leftRightTurns)
        #print(followed)
    if applereset == 0:
        for i in range (int(w) - 5, int(w) + 5):
            if (i > snake.xcor() - 5) and (i < snake.xcor() + 5):
                for j in range (int(z) - 5, int(z) + 5):
                    if (j > snake.ycor() - 5) and (j < snake.ycor() + 5):
                        if ateApple == False:
                            resetcOrds()
    if ateApple == True:
            score += 1
            scorestring = "Score: %s" %score
            mypen.undo()
            mypen.write(scorestring, font=("Arial",14, "normal"))
            applereset = 0
            oldspeed = speed
            speed = oldspeed + 0.5
            tailspeed = speed - 1
            ateApple = False                                 

apple.listen()

#-------------------------------------debug code-------------------------------
##    print("turns", turns)
##    print("coords list", coords)
##    print("snake coords", snake.xcor(), snake.ycor()) 
##    print("snaketail coords", snaketail.xcor(), snaketail.ycor())
##    print("\n")
