"""This is a  generator."""
import turtle


class Ball:
    def __init__(self):

        self.ball = turtle.Turtle()     # Creates "Turtle object".

        """Settings:"""
        self.ball.speed(0)              # Sets paddle speed (0 = Max speed).
        self.ball.shape("square")       # Sets paddle shape.
        self.ball.color("white")        # Sets paddle color.

        self.ball.penup()               # To avoid drawing line while moving.
        self.ball.goto(0, 0)            # Sets starting position.

        self.ball.dx = 5                # Horizontal movement.
        self.ball.dy = 5                # Vertical movement.
