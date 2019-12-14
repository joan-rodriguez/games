"""This file generates window objects. <- LIAR"""
import time
import turtle

import pygame
from pong.ball import Ball
from pong.paddle import Paddle


def check_point(ball, width_screen):
    point_scored = None

    if ball.xcor() > (width_screen / 2 - 10):
        point_scored = 1

        ball.reset_position()
        ball.reset_velocity(1)

    if ball.xcor() < (-(width_screen / 2 - 10)):
        point_scored = 2

        ball.reset_position()
        ball.reset_velocity(-1)

    return point_scored


def check_velocity_increase(ball, playing_time):
    if playing_time > 10:
        ball.increment_velocity()
        return True

    return False


def create_window(title, wid, hei):
    """Creates a window with specific settings."""
    win = turtle.Screen()  # Creates one window

    # Settings:
    win.title(title)  # Sets title.

    win.bgcolor("black")  # Background color.
    win.setup(width=wid, height=hei)  # Width and height in pixels.

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
    score = {
        1: 0,
        2: 0
    }

    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, wn_height / 2 - 40)
    pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "bold"))

    while True:
        wn.update()
        clock.tick(24)

        playing_time = time.time() - start_time

        # Move the ball around, check borders and act accordingly
        if check_velocity_increase(ball, playing_time):
            start_time = time.time()

        point = check_point(ball, wn_width)

        if point:
            score[point] += 1
            write_score(pen, score)

        # Paddle and ball collisions
        ball.collisions(paddle_a, paddle_b)


def write_score(pen, score):
    pen.clear()
    pen.write(
        "Player A: {}  Player B: {}".format(score[0], score[1]),
        align="center",
        font=("Courier", 24, "bold")
    )
