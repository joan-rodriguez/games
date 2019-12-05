"""This file generates window objects."""
import turtle
from paddle import Paddle
from ball import Ball


def create_window(title):
    """Creates a window with specific settings."""
    win = turtle.Screen()                    # Creates one window

    """Settings:"""
    win.title(title)                         # Sets title.

    win.bgcolor("black")                     # Background color.
    win.setup(width=800, height=600)         # Width and height in pixels.

    win.tracer(0)
    win.listen()

    return win

wn = create_window("Pong")

# Paddle A
paddle_a = Paddle("A", -350, 0)
wn.onkeypress(paddle_a.paddle_up, "w")
wn.onkeypress(paddle_a.paddle_down, "s")

# Paddle B
paddle_b = Paddle("B", 350, 0)
wn.onkeypress(paddle_b.paddle_up, "Up")
wn.onkeypress(paddle_b.paddle_down, "Down")

# Ball
ball = Ball()

while True:
    wn.update()
