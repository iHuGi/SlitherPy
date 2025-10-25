from turtle import Screen
from scoreboard import Scoreboard
from snake import Snake
from food import Food
import _tkinter
import time

# Initialize game screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # Turns off automatic screen updates for smoother animation

# Create game objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Set up key listeners for snake movement
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
try:
    while game_is_on:
        """
        Main game loop:
        - Updates the screen
        - Moves the snake
        - Detects collision with food and refreshes food position
        """
        screen.update()  # Update the screen
        time.sleep(0.1)
        snake.move()

        # Check for collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend_snake()
            scoreboard.increase_score()

        # Detect collision with wall
        if abs(snake.head.xcor()) > 280 or abs(snake.head.xcor()) < -280 or abs(snake.head.ycor()) > 280 or abs(snake.head.ycor()) < -280:
            scoreboard.game_over()
            game_is_on = False
            screen.update()
            time.sleep(2)

        # Detect collision with tale
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.game_over()
                game_is_on = False
                screen.update()
                time.sleep(2)

except _tkinter.TclError:
    print("Game closed. Exiting gracefully.")
except KeyboardInterrupt:
    print("\nGame interrupted by user. Exiting...")

# Close the screen properly after the game ends
finally:
    try:
        screen.bye()  # Ensures the game window closes properly
    except _tkinter.TclError:
        pass