"""This is a paddle generator."""
import turtle


class Paddle:
    def __init__(self, player, pos_x):

        self.paddle = turtle.Turtle()   # Creates "Turtle object".
        self.player = player            # Specific player.

        """Settings:"""
        self.paddle.speed(0)            # Sets paddle speed (0 = Max speed).
        self.paddle.shape("square")     # Sets paddle shape.
        self.paddle.color("white")      # Sets paddle color.
        self.paddle_wid = 5
        self.paddle.shapesize(stretch_wid=self.paddle_wid, stretch_len=1)     # Sets bar-shape.

        self.paddle.penup()             # To avoid drawing line while moving.

        self.pos_x = pos_x
        self.pos_y = 0
        self.paddle.goto(self.pos_x, self.pos_y)  # Sets starting position.

    def paddle_up(self):
        y = self.paddle.ycor()
        y += 20
        self.paddle.sety(y)

    def paddle_down(self):
        y = self.paddle.ycor()
        y -= 20
        self.paddle.sety(y)

    def position_y(self):
        return self.paddle.ycor()
