# Import necessary modules
from turtle import Turtle

# === PLAYER CONSTANTS ===
STARTING_POSITION = (0, -280)  # Player's starting position at bottom center of screen
MOVE_DISTANCE = 10             # Distance player moves with each key press
FINISH_LINE_Y = 280            # Y-coordinate of the finish line at top of screen

class Player(Turtle):
    """
    Player turtle that moves up the screen to cross the finish line.
    Inherits from Turtle class to get all turtle graphics functionality.
    """

    def __init__(self):
        """Initialize the player turtle with starting position and orientation."""
        super().__init__()  # Initialize parent Turtle class
        self.shape("turtle")  # Set player appearance to turtle shape
        self.penup()         # Don't draw lines when moving
        self.go_to_start()   # Position player at starting location
        self.setheading(90)  # Point turtle upward (90 degrees = north)

    def move_up(self):
        """
        Move the player upward by MOVE_DISTANCE pixels.
        This method is called when the Up arrow key is pressed.
        """
        self.forward(MOVE_DISTANCE)  # Move forward in current direction (upward)
        
    def crossed_success(self):
        """
        Check if the player has successfully crossed the finish line.
        
        Returns:
            bool: True if player's y-coordinate is above the finish line, False otherwise
        """
        if self.ycor() > FINISH_LINE_Y:  # Check if player is above finish line
            return True
        else:
            return False

    def go_to_start(self):
        """
        Reset the player's position back to the starting point.
        Called at game start and after successfully crossing the finish line.
        """
        self.goto(STARTING_POSITION)  # Move player to starting coordinates (0, -280)
