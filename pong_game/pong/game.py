"""This file generates window objects."""
import turtle
from paddle import Paddle
from ball import Ball


def create_window(title):
    """Creates a window with specific settings."""
    wn = turtle.Screen()                    # Creates one window

    """Settings:"""
    wn.title(title)                         # Sets title.

    wn.bgcolor("black")                     # Background color.
    wn.setup(width=800, height=600)         # Width and height in pixels.

    wn.tracer(0)

    return wn

wn = create_window("Pong")

# Paddle A
paddle_a = Paddle("A", -350, 0)

# Paddle B
paddle_b = Paddle("B", 350, 0)

# Ball
ball = Ball()

wn.listen()
wn.onkeypress(paddle_a.paddle_up(), "w")

while True:
    wn.update()
