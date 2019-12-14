"""This is a paddle generator."""
import turtle


# Inheritance
class Paddle(turtle.Turtle):

    # Class attribute
    paddle_wid = 5
    delta = 20  # Define the pixels to move each time.

    def __init__(self, player, init_pos_x, init_pos_y=0):
        super().__init__()

        # Instance attributes
        self.player = player  # Specific player.

        # Bring to init position
        self.initialise_paddle(init_pos_x, init_pos_y)

    def initialise_paddle(self, init_pos_x, init_pos_y):
        """Initialise paddle parameters & bring it to starting point."""
        self.speed(0)  # Sets paddle speed (0 = Max speed).
        self.shape("square")  # Sets paddle shape.
        self.color("white")  # Sets paddle color.
        self.shapesize(stretch_wid=self.paddle_wid, stretch_len=1)  # Sets bar-shape.
        self.penup()  # To avoid drawing line while moving.

        # Sets starting position.
        self.setx(init_pos_x)
        self.sety(init_pos_y)

    def paddle_up(self):
        self.sety(
            self.ycor() + self.delta
        )

    def paddle_down(self):
        self.sety(
            self.ycor() - self.delta
        )

    # Getter
    def get_position_y(self):
        return self.ycor()
