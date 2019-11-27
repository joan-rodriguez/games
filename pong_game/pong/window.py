"""This file generates window objects."""
import turtle
from pong.paddle import Paddle


class Window:
    def __init__(self, title):

        self.wn = turtle.Screen()               # Creates one window.

        """Settings:"""
        self.title = title                      # Sets title.
        self.wn.title(self.title)

        self.wn.bgcolor("black")                # Background color.
        self.wn.setup(width=800, height=600)    # Width and height in pixels.

        self.wn.tracer(0)

    def update(self):
        self.wn.update()
