"""This is a  generator."""
import os
import time
import turtle


class Ball(turtle.Turtle):

    dx_init = 5
    dy_init = 5

    def __init__(self):
        super().__init__()

        self.dx = self.dy = None

        self.initialize_ball()

    def initialize_ball(self):
        """Initialize ball parameters & bring it to starting position."""
        self.speed(0)  # Sets paddle speed (0 = Max speed).
        self.shape("square")  # Sets paddle shape.
        self.color("white")  # Sets paddle color.
        self.penup()  # To avoid drawing line while moving.
        self.goto(0, 0)  # Sets starting position.

        self.dx = self.dx_init  # Horizontal movement.
        self.dy = self.dy_init  # Vertical movement.

    @staticmethod
    def play_sound():
        os.system("aplay pong/bounce.wav&")

    def move(self):
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)

    def increment_velocity(self):
        self.dx *= 1.2
        self.dy *= 1.2

    def reset_velocity(self, direction):
        self.dx = direction * self.dx_init  # Horizontal movement.
        self.dy = self.dy_init  # Vertical movement.

    def reset_position(self):
        self.goto(0, 0)
        self.dx *= -1

    def check_border(self, width_screen, height_screen, pen, score):
        if self.ball.ycor() > (height_screen / 2 - 10):
            self.ball.sety(height_screen / 2 - 10)
            self.ball.dy *= -1
            self.play_sound()

        if self.ball.ycor() < (-(height_screen / 2 - 10)):
            self.ball.sety(-(height_screen / 2 - 10))
            self.ball.dy *= -1



        return score

    def collisions(self, paddle_a, paddle_b):
        if self.ball.xcor() > (paddle_b.pos_x - 10) \
                and (paddle_b.get_position_y() - 50) < self.ball.ycor() < (paddle_b.get_position_y() + 50):
            self.ball.setx(paddle_b.pos_x - 10)
            self.ball.dx *= -1
            self.play_sound()

        if self.ball.xcor() < (paddle_a.pos_x + 10) \
                and (paddle_a.get_position_y() - 50) < self.ball.ycor() < (paddle_a.get_position_y() + 50):
            self.ball.setx(paddle_a.pos_x + 10)
            self.ball.dx *= -1
            self.play_sound()
