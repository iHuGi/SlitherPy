from turtle import Turtle
import random

class Food(Turtle):
    """
    Represents the food in the Snake game.
    Inherits from Turtle and randomly positions itself on the screen.
    """

    def __init__(self):
        """Initialize the food as a small blue circle and place it at a random position."""
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Makes the food smaller
        self.color("blue")
        self.speed("fastest")  # Ensures instant movement when repositioning
        self.refresh()  # Place food at a random location at start

    def refresh(self):
        """Move the food to a new random location on the screen."""
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)