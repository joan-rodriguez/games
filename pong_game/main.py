"""Simple Pong game."""
import turtle
from pong.ball import Ball
from pong.paddle import Paddle
from pong.window import Window

# Window
wn = Window("Pong")

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
    input('Press enter when finished.')
    exit()
