# Import necessary modules
from turtle import Turtle

# === DISPLAY CONSTANTS ===
FONT = ("Courier", 24, "normal")  # Font style, size, and weight for text display

class Scoreboard(Turtle):
    """
    Manages the game's scoreboard display including level tracking and game over screen.
    Inherits from Turtle class to use text writing capabilities.
    """

    def __init__(self):
        """Initialize the scoreboard with starting values and position."""
        super().__init__()  # Initialize parent Turtle class
        
        # Game tracking variables
        self.score = 0   # Current score (currently unused but available for future features)
        self.level = 1   # Current level (starts at level 1)
        
        # Configure turtle for text display
        self.hideturtle()  # Don't show the turtle cursor/shape
        self.penup()       # Don't draw lines when moving
        
        # Position scoreboard at top-left corner of screen
        self.goto(-280, 250)  # Move to upper-left area (x=-280, y=250)
        
        # Display initial scoreboard
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Refresh the scoreboard display with current level information.
        Clears previous text and writes updated level.
        """
        self.clear()  # Remove previous text from screen
        self.write(f"Level: {self.level}", align="left", font=FONT)  # Write current level

    def increase_level(self):
        """
        Increment the level counter and refresh the display.
        Called when player successfully crosses the finish line.
        """
        self.level += 1           # Increase level by 1
        self.update_scoreboard()  # Update display with new level

    def game_over(self):
        """
        Display game over message in the center of the screen.
        Called when player collides with a car.
        """
        self.goto(0, 0)  # Move to center of screen (x=0, y=0)
        self.write("GAME OVER", align="center", font=FONT)  # Display game over text
