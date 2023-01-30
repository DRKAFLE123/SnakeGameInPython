import turtle
import random
import time

delay = 0.1
score = 0
HighestScore=0

#snakebodies
bodies=[] #list to store body

#Getting a screen | canvas to play game
s = turtle.Screen()
s.title("Snake Game")
s.bgcolor("gray")
s.setup(width=600,height=600)


#Create snake head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("White")
head.fillcolor("Blue")
head.penup()
head.goto(0,0)
head.direction="stop"

#Now we will make snake food
food=turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("yellow")
food.fillcolor("green")
food.penup()
food.ht()  #hide turtle ht()
food.goto(0,200)
food.st()  #show turtle st()

#score board
sb=turtle.Turtle()
sb.shape("square")
sb.fillcolor("black")
sb.penup()
sb.ht()
sb.goto(-250,-250)
sb.write("Score:0| Highest Score: 0")

def moveup():
    if head.direction!="down":
        head.direction="up"
def movedown():      
    if head.direction!="up":
        head.direction="down"
def moveleft():
    if head.direction!="right":
        head.direction="left"
def moveright():
    if head.direction!="left":
        head.direction="right"
def stop():
    head.direction="stop"
def move():
    if head.direction=="up":
       y=head.ycor()
       head.sety(y+20)
        
    if head.direction=="down":
       y=head.ycor()
       head.sety(y-20)
    
    if head.direction=="left":
       x=head.xcor()
       head.setx(x-20)
    
    if head.direction=="right":
       x=head.xcor()
       head.setx(x+20)

#Event Handling-key mappings
s.listen()
s.onkey(moveup,"up")
s.onkey(movedown,"down")
s.onkey(moveleft,"left")
s.onkey(moveright,"right")
s.onkey(stop,"space")

# main loop
while True:
    s.update() #this will update the screen
    #check the collission with border
    if head.xcor()>290:
        head.setx(-290)
    if head.xcor()<-290:
        head.setx(290)
    if head.ycor()>290:
        head.sety(-290)
    if head.ycor()<-290:
        head.sety(290)
#check collission with food
    if head.distance(food)<20:
        #move food to random
       x=random.randint(-290,290)
       y=random.randint(-290,290)
       food.goto(x,y)

       #increase the length of the snake
       body=turtle.Turtle()
       body.speed()
       body.penup()
       body.shape("square")
       body.color("red")
       body.fillcolor("black")
       bodies.append(body)  #add the new body unit

       #increase the score
       score+=10

       #chane delay
       delay-=0.001
       #update the highest score
       if score>HighestScore:
           sb.clear()
           sb.write("Score:{} Highest Score:{}".format(score,HighestScore))

           #move the snake bodies
    for index in range(len(bodies)-1,0,-1):
        x=bodies[index-1].xcor()
        y=bodies[index-1].ycor()
        bodies[index].goto(x,y)

    if len(bodies)>0:
        x=head.xcor()
        y=head.ycor()
        bodies[0].goto(x,y)
    move()

        #check collission with snake body
    for body in bodies:
        if body.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"
        #hide bodies
            for body in bodies:
                body.ht()
            bodies.clear()

            score=0
            delay=0.1

       #update score board
            sb.clear()
            sb.write("Score: {} Highest Score:{}".format(score,HighestScore))
    time.sleep(delay)
s.mainloop()

#this is the end of our snake game