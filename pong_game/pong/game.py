"""This file generates window objects."""
import pygame
import time
import turtle
from pong.paddle import Paddle
from pong.ball import Ball


def create_window(title, wid, hei):
    """Creates a window with specific settings."""
    win = turtle.Screen()                    # Creates one window

    """Settings:"""
    win.title(title)                         # Sets title.

    win.bgcolor("black")                     # Background color.
    win.setup(width=wid, height=hei)         # Width and height in pixels.

    win.tracer(0)
    win.listen()

    return win

def start_game():
    wn_width = 800
    wn_height = 600
    wn = create_window("Pong", wn_width, wn_height)
    clock = pygame.time.Clock()
    start_time = time.time()

    # Paddle A
    paddle_a = Paddle("A", -(wn_width / 2 - 50))
    wn.onkeypress(paddle_a.paddle_up, "w")
    wn.onkeypress(paddle_a.paddle_down, "s")

    # Paddle B
    paddle_b = Paddle("B", wn_width / 2 - 50)
    wn.onkeypress(paddle_b.paddle_up, "Up")
    wn.onkeypress(paddle_b.paddle_down, "Down")

    # Ball
    ball = Ball()

    # Scoreboard
    score = [0, 0]          # Score [Player_A, Player_B]
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, wn_height/2 - 40)
    pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "bold"))

    while True:
        wn.update()
        clock.tick(24)
        playing_time = time.time() - start_time

        # Move the ball around, check borders and act accordingly
        start_time = ball.move(start_time, playing_time)
        score = ball.check_border(wn_width, wn_height, pen, score)

        # Paddle and ball collisions
        ball.collisions(paddle_a, paddle_b)
