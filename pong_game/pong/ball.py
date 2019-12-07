"""This is a  generator."""
import os
import time
import turtle


class Ball:
    def __init__(self):

        self.ball = turtle.Turtle()  # Creates "Turtle object".

        """Settings:"""
        self.ball.speed(0)  # Sets paddle speed (0 = Max speed).
        self.ball.shape("square")  # Sets paddle shape.
        self.ball.color("white")  # Sets paddle color.

        self.ball.penup()  # To avoid drawing line while moving.
        self.ball.goto(0, 0)  # Sets starting position.

        self.ball.dx_init = 5
        self.ball.dy_init = 5

        self.ball.dx = self.ball.dx_init  # Horizontal movement.
        self.ball.dy = self.ball.dy_init  # Vertical movement.

    def move(self, start_time, playing_time):
        if playing_time > 10:
            self.ball.dx *= 1.2
            self.ball.dy *= 1.2
            start_time = time.time()

        self.ball.setx(self.ball.xcor() + self.ball.dx)
        self.ball.sety(self.ball.ycor() + self.ball.dy)

        return start_time

    def reset_velocity(self):
        self.ball.dx = self.ball.dx_init  # Horizontal movement.
        self.ball.dy = self.ball.dy_init  # Vertical movement.

    def check_border(self, width_screen, height_screen, pen, score):
        if self.ball.ycor() > (height_screen / 2 - 10):
            self.ball.sety(height_screen / 2 - 10)
            self.ball.dy *= -1
            os.system("aplay pong/bounce.wav&")

        if self.ball.ycor() < (-(height_screen / 2 - 10)):
            self.ball.sety(-(height_screen / 2 - 10))
            self.ball.dy *= -1
            os.system("aplay pong/bounce.wav&")

        if self.ball.xcor() > (width_screen / 2 - 10):
            self.ball.goto(0, 0)
            self.ball.dx *= -1
            self.reset_velocity()
            score[0] += 1
            pen.clear()
            pen.write("Player A: {}  Player B: {}".format(score[0], score[1]), align="center",
                      font=("Courier", 24, "bold"))

        if self.ball.xcor() < (-(width_screen / 2 - 10)):
            self.ball.goto(0, 0)
            self.ball.dx *= -1
            self.reset_velocity()
            score[1] += 1
            pen.clear()
            pen.write("Player A: {}  Player B: {}".format(score[0], score[1]), align="center",
                      font=("Courier", 24, "bold"))

        return score

    def collisions(self, paddle_a, paddle_b):
        if self.ball.xcor() > (paddle_b.pos_x - 10) \
                and (paddle_b.position_y() - 50) < self.ball.ycor() < (paddle_b.position_y() + 50):
            self.ball.setx(paddle_b.pos_x - 10)
            self.ball.dx *= -1
            os.system("aplay pong/bounce.wav&")

        if self.ball.xcor() < (paddle_a.pos_x + 10) \
                and (paddle_a.position_y() - 50) < self.ball.ycor() < (paddle_a.position_y() + 50):
            self.ball.setx(paddle_a.pos_x + 10)
            self.ball.dx *= -1
            os.system("aplay pong/bounce.wav&")
