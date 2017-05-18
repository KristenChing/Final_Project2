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
turns = 0
speed = 2
tailspeed = 1
ateApple = False
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
def resetcOrds():
    #apple.hideturtle()
    global w
    w = apple.xcor()
    global z
    z = apple.ycor()
    apple.goto(random.randint(-100, 100), random.randint(-100, 100))
    #apple.showturtle()
resetcOrds()  

def left():
    global turnedLeft
    global turns
    turns += 1
    snake.left(90)
    resetcoords()
    turnedLeft = True
def right():
    global turnedRight
    global turns
    turns += 1
    snake.right(90)
    resetcoords()
    turnedRight = True
turtle.listen()
turtle.onkey(left, "Left")
turtle.onkey(right, "Right")
while True:
    snake.forward(speed)
    snaketail.forward(tailspeed)
##    print(speed)
##    print("tail", tailspeed)
##    print("turns", turns)
##    print("coords list", coords)
    print("snake coords", snake.xcor(), snake.ycor()) 
##    print("snaketail coords", snaketail.xcor(), snaketail.ycor())
    print("apple coords", apple.xcor(), apple.ycor()) 
    print("\n")
    x = snake.xcor()
    y = snake.ycor()
    w = apple.xcor()
    z = apple.ycor()
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
    for i in range (int(w) - 10, int(w) + 10):
        print("w", w)
        print("i", i)
        if i == snake.xcor():
            for j in range (int(z) - 10, int(z) + 10):
                print("j", j)
                if j == snake.ycor():
                    apple.hideturtle()
                    apeat+=1
                    ateApple = True
                    resetcOrds()
                    apple.showturtle()
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
