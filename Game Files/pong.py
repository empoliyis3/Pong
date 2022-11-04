from turtle import Screen, Turtle
from time import sleep

SMALL_FONT = ("Courier", 30, "normal")
BIG_FONT = ("Courier", 60, "normal")
MENU_FONT = ("a Absolute Empire", 60, "normal")

WINDOW_WIDTH, WINDOW_HEIGHT = 1920, 1080

fd_list = [(90, WINDOW_HEIGHT/2), (0, WINDOW_WIDTH/2), (270, WINDOW_HEIGHT), (180, WINDOW_WIDTH), (90, WINDOW_HEIGHT), (0, WINDOW_WIDTH/2)]

def clickStart(x, y):
    if startGame.xcor() - 200 < x < startGame.xcor() + 200 and startGame.ycor() - 75 < y < startGame.ycor() + 75:
        screen.onscreenclick(None)
        sleep(0.5)

        mainTitle.clear()
        screen.bgcolor("black")
        startGame.hideturtle()

        # Get rid of Main Menu 
        mainCanvas.clear()
        startGame.hideturtle()

        # Moves Paddle A(1) up and down the y axis with (w) and (s) key respectively
        screen.onkeypress(paddleAUp, "w")
        screen.onkeypress(paddleADown, "s")
        paddleA.showturtle()

        # Moves Paddle B(2) up and down the y axis with (Up_Arrow) and (Down_Arrow) key respectively
        screen.onkeypress(paddleBUp, "Up")
        screen.onkeypress(paddleBDown, "Down")
        paddleB.showturtle()

        ball.showturtle()

        screen.listen()
        
        play()

# Movings Functions
# Paddle A Up with (w) key for player A(1)
def paddleAUp():
    paddleA.forward(20)

# Paddle A Down with (s) Key for player A(1)
def paddleADown():
    paddleA.backward(20)

# Paddle B Up with (Up_Arrow) Key for player B(2)
def paddleBUp():
    paddleB.forward(20)

# Paddle B Down (Down_Arrow) key for player B(2)
def paddleBDown():
    paddleB.backward(20)

# Scores
AScore = 0
BScore = 0

# Main Loop To check canvas and update it each millisecond
def play():
    global AScore, BScore

    # Make Ball Move
    ball.setx(ball.xcor() + ball.x)
    ball.sety(ball.ycor() + ball.y)

    # Ball Bouncing when it hits edge
    if ball.ycor() > 510:
        ball.sety(510)
        ball.y *= -1
    elif ball.ycor() < -510:
        ball.sety(-510)
        ball.y *= -1

    # Counting scoring system, when Ball goes Behind Paddle the Ball Resets and Goes in the Other Direction
    # Which will then update the Score Text at the upper Left Corner
    if ball.xcor() > 950:
        ball.goto(0, 0)
        ball.x *= -1
        AScore += 1
        ScoreSystemA.clear()
        ScoreSystemA.write(f"P1 Score: {AScore}", align='center', font=SMALL_FONT)

    elif ball.xcor() < -950:
        ball.goto(0, 0)
        ball.x *= -1
        BScore += 1
        ScoreSystemB.clear()
        ScoreSystemB.write(f"P2 Score: {BScore}", align='center', font=SMALL_FONT)

    #Winning and Updating Score
    if AScore == 3:
        midLine.clear()
        ball.hideturtle()
        AWin = Turtle()
        AWin.hideturtle()
        AWin.pencolor("White")
        AWin.write("P1 Wins!", align="center", font=BIG_FONT)
        screen.update()
        return

    if BScore == 3:
        midLine.clear()
        ball.hideturtle()
        BWin = Turtle()
        BWin.hideturtle()
        BWin.pencolor("White")
        BWin.write("P2 Wins!", align="center", font=BIG_FONT)
        screen.update()
        return

    if -950 < ball.xcor() < -900 and paddleA.ycor() - 72 < ball.ycor() < paddleA.ycor() + 72:
        ball.x *= -1
    elif 900 < ball.xcor() < 950 and paddleB.ycor() - 72 < ball.ycor() < paddleB.ycor() + 72:
        ball.x = ball.x * -1

    screen.update()
    screen.ontimer(play)

screen = Screen()
screen.title("My First Project")
screen.bgcolor("black")
screen.setup(WINDOW_WIDTH, WINDOW_HEIGHT)
# screen.register_shape("start_400x150.gif")  # PNG for start button
screen.tracer(0)

# Create Paddle A, Player 1 (left Side)
paddleA = Turtle()
paddleA.hideturtle()
paddleA.shape("square")
paddleA.shapesize(1, 9)
paddleA.color("white")
paddleA.penup()
paddleA.setheading(90)
paddleA.setx(-900)

# Create Paddle B, Player 2 (Right Side)
paddleB = paddleA.clone()
paddleB.setx(900)

# Create Ball making it move in diagonal direction in fixed speed
ball = Turtle()
ball.hideturtle()
ball.shape("square")
ball.color("white")
ball.shapesize(1.8)
ball.penup()

ball.x = 3  # user properties
ball.y = 3

# Middle Line
midLine = Turtle()
midLine.hideturtle()
midLine.color("white")
midLine.pensize(2)
midLine.penup()
midLine.sety(-WINDOW_HEIGHT/2)
midLine.pendown()
midLine.sety(WINDOW_HEIGHT/2)

# Scoring System for Player A(1)
ScoreSystemA = Turtle()
ScoreSystemA.hideturtle()
ScoreSystemA.color("White")
ScoreSystemA.penup()
ScoreSystemA.setposition(-480, 420)
ScoreSystemA.write(f"P1 Score: {AScore}", align='center', font=SMALL_FONT)

# Scoring System for Player B(2)
ScoreSystemB = Turtle()
ScoreSystemB.hideturtle()
ScoreSystemB.color("White")
ScoreSystemB.penup()
ScoreSystemB.setposition(480, 420)
ScoreSystemB.write(f"P2 Score: {BScore}", align='center', font=SMALL_FONT)

# Create Menu
mainCanvas = Turtle()
mainCanvas.hideturtle()
mainCanvas.color("cyan")
mainCanvas.begin_fill()

for heading, distance in fd_list:
    mainCanvas.setheading(heading)
    mainCanvas.forward(distance)

mainCanvas.end_fill()

# Create Title
mainTitle = Turtle()
mainTitle.hideturtle()
mainTitle.penup()
mainTitle.sety(270)
mainTitle.write("Main Menu", align="center", font=MENU_FONT)

# Create Start Option
startGame = Turtle()
startGame.penup()
startGame.sety(100)
screen.addshape("D:\Pong Game\Pong\Game Files\start.gif")
startGame.shape("D:\Pong Game\Pong\Game Files\start.gif")
# Key Binding Main Menu
screen.onscreenclick(clickStart)

screen.update()
screen.mainloop()

    
    
    

    
