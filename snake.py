from turtle import Turtle

# Constants for snake behavior
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  # Initial 3-segment snake
MOVE_DISTANCE = 20  # Distance each segment moves per step
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    """Represents the snake in the game, handling movement and direction changes."""

    def __init__(self):
        """Initialize the snake with three segments and set the head reference."""
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Creates the initial snake with predefined starting positions."""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend_snake(self):
        """Adds new segment to the snake"""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Moves the snake forward by shifting each segment to the position of the previous one."""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Changes direction to up unless currently moving down."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Changes direction to down unless currently moving up."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Changes direction to left unless currently moving right."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Changes direction to right unless currently moving left."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)