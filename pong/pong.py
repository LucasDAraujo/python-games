import turtle
from playsound import playsound


# Window config
wn = turtle.Screen()
wn.title("Pong by @LucasDAraujo")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1,)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1,)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
# Every move is 2 pixels(dx,dy)
BALL_SPEED_X = 0.1
BALL_SPEED_Y = -0.1
ball.dx = BALL_SPEED_X
ball.dy = BALL_SPEED_Y

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"Player A: 0  Player B: 0", align="center",
          font=("Courier", 18, "normal"))

# FUNCTIONS


def write_score():
    pen.clear()
    pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center",
              font=("Courier", 18, "normal"))


def write_message(message):
    pen.clear()
    pen.write(f"{message}", align="center",
              font=("Courier", 18, "normal"))


def paddle_a_up():
    if paddle_a.ycor() < 240:
        y = paddle_a.ycor()
        y += 20
        paddle_a.sety(y)


def paddle_a_down():
    if paddle_a.ycor() > -240:
        y = paddle_a.ycor()
        y -= 20
        paddle_a.sety(y)


def paddle_b_up():
    if paddle_b.ycor() < 240:
        y = paddle_b.ycor()
        y += 20
        paddle_b.sety(y)


def paddle_b_down():
    if paddle_b.ycor() > -240:
        y = paddle_b.ycor()
        y -= 20
        paddle_b.sety(y)


# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, 'w')
wn.onkeypress(paddle_a_down, 's')
wn.onkeypress(paddle_b_up, 'Up')
wn.onkeypress(paddle_b_down, 'Down')

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        playsound('bounce.wav', False)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        playsound('bounce.wav', False)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        write_score()

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        write_score()

    # Paddle and ball colisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        playsound('bounce.wav', False)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        playsound('bounce.wav', False)

    if score_a == 5 or score_b == 5:
        if score_a > score_b:
            write_message("Player A wins!!!")
        else:
            write_message("Player B wins!!!")
        playsound("win.mp3")
        break
