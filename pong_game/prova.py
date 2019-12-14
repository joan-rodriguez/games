import os
import turtle

import pygame


def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Windows
wn = turtle.Screen()  # Creates one window.
wn.title("prova")
wn.bgcolor("black")  # Background color.
width_screen = 800
height_screen = 600
wn.setup(width=width_screen, height=height_screen)  # Width and height in pixels.
wn.tracer(0)
wn.update()
clock = pygame.time.Clock()

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()  # Creates "Turtle object".
paddle_a.speed(0)  # Sets paddle speed (0 = Max speed).
paddle_a.shape("square")  # Sets paddle shape.
paddle_a.color("white")  # Sets paddle color.
paddle_a.shapesize(stretch_wid=5, stretch_len=1)  # Sets bar-shape.
paddle_a.penup()  # To avoid drawing line while moving.
paddle_a_init = -(width_screen / 2 - 50)
paddle_a.goto(paddle_a_init, 0)  # Sets starting position.

# Paddle B
paddle_b = turtle.Turtle()  # Creates "Turtle object".
paddle_b.speed(0)  # Sets paddle speed (0 = Max speed).
paddle_b.shape("square")  # Sets paddle shape.
paddle_b.color("white")  # Sets paddle color.
paddle_b.shapesize(stretch_wid=5, stretch_len=1)  # Sets bar-shape.
paddle_b.penup()  # To avoid drawing line while moving.
paddle_b_init = width_screen / 2 - 50
paddle_b.goto(paddle_b_init, 0)  # Sets starting position.

# Ball
ball = turtle.Turtle()  # Creates "Turtle object".
ball.speed(0)  # Sets paddle speed (0 = Max speed).
ball.shape("square")  # Sets paddle shape.
ball.color("white")  # Sets paddle color.
ball.penup()  # To avoid drawing line while moving.
ball.goto(0, 0)  # Sets starting position.
ball.dx = 5
ball.dy = 5

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, height_screen / 2 - 40)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "bold"))

wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

while True:
    wn.update()
    clock.tick(24)

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > (height_screen / 2 - 10):
        ball.sety(height_screen / 2 - 10)
        ball.dy *= -1
        self.play_sound()

    if ball.ycor() < (-(height_screen / 2 - 10)):
        ball.sety(-(height_screen / 2 - 10))
        ball.dy *= -1
        self.play_sound()

    if ball.xcor() > (width_screen / 2 - 10):
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "bold"))

    if ball.xcor() < (-(width_screen / 2 - 10)):
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "bold"))

    # Paddle and ball collisions
    if ball.xcor() > (paddle_b_init - 10) \
            and (paddle_b.ycor() + 50) > ball.ycor() > (paddle_b.ycor() - 50):
        ball.setx(paddle_b_init - 10)
        ball.dx *= -1
        self.play_sound()

    if ball.xcor() < (paddle_a_init + 10) \
            and (paddle_a.ycor() + 50) > ball.ycor() > (paddle_a.ycor() - 50):
        ball.setx(paddle_a_init + 10)
        ball.dx *= -1
        self.play_sound()
