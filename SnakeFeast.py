import turtle
import random
import time

# Game Variables
delay = 0.1
sc = 0  # Score
hs = 0  # High Score
bodies = []  # List to store snake body parts

# Creating Game Screen
scr = turtle.Screen()
scr.title("🐍 Snake Feast 🐍")
scr.bgcolor("green")
scr.setup(width=1200, height=850)
scr.tracer(0)  # Turns off screen updates for smooth gameplay

# Creating Snake Head
head=turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("blue")
#head.fillcolor("blue")
head.penup()
head.goto(0,0)
head.direction="stop"

# Creating Food for Snake
food=turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("yellow")
food.penup()
food.goto(150,200)

# Creating Scoreboard
sb=turtle.Turtle()
sb.speed(0)
sb.color("black")
sb.penup()
sb.hideturtle()
sb.goto(0,350)  

# Function to Update Scoreboard
def update_score():
    sb.clear()  # Clear previous score
    sb.write("Score Card: {}    |   Highest Score: {}".format(sc, hs),
             align="center", font=("Courier", 18, "bold"))

update_score()  # Initial Score Display

# Functions to Move in All Directions
def moveUp():
    if head.direction != "down":
        head.direction = "up"

def moveDown():
    if head.direction !="up":
        head.direction ="down"

def moveLeft():
    if head.direction !="right":
        head.direction ="left"

def moveRight():
    if head.direction !="left":
        head.direction ="right"
def moveStop():
     head.direction="stop"

def move():
    if head.direction =="up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x=head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x=head.xcor()
        head.setx(x+20)
        
# Event Handling for Key Presses
scr.listen()
scr.onkey(moveUp,"Up")
scr.onkey(moveDown,"Down")
scr.onkey(moveLeft,"Left")
scr.onkey(moveRight,"Right")
scr.onkey(moveStop,"space")

# Main  Loop
while True:
    scr.update()

    # Check Collision with Border 
    if head.xcor()>290:
        head.setx(-290)
    if head.xcor()<-290:
        head.setx(290)
    if head.ycor()>290:
        head.sety(-290)
    if head.ycor()<-290:
        head.sety(290)

    # Check Collision with Food
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)

        # Increase the body of snake
        body = turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("square")
        body.color("red")
        bodies.append(body)

        sc=sc+10  # Increase score
        delay=delay-0.001  # Increase speed

        if sc > hs:
            hs = sc  # Update highest score
        update_score()  # Update scoreboard
            
    # Move snake bodies
    for i in range(len(bodies)-1, 0, -1):
        x = bodies[i-1].xcor()
        y = bodies[i-1].ycor()
        bodies[i].goto(x,y)
    
    if len(bodies) > 0:
        x = head.xcor()
        y = head.ycor()
        bodies[0].goto(x,y)

    move()

    # Check collision with snake body
    for body in bodies:
        if body.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction ="stop"

            # Hide bodies
            for body in bodies:
                body.hideturtle()
            bodies.clear()

            sc = 0  # Reset score
            delay = 0.1  # Reset speed
            update_score()  # Reset scoreboard

    time.sleep(delay)

scr.mainloop()

































