# Import necessary modules
from turtle import Turtle
import random

# === GAME CONSTANTS ===
COLORS = ['red', "orange", "yellow", "green", "blue", "purple"]  # Available car colors
STARTING_MOVE_DISTANCE = 5  # Initial speed of cars (pixels per frame)
MOVE_INCREMENT = 5          # Speed increase when leveling up

class CarManager():
    """
    Manages all cars in the game including creation, movement, and speed control.
    """

    def __init__(self):
        """Initialize the car manager with empty car list and starting speed."""
        self.all_cars = []  # List to store all car objects
        self.car_speed = STARTING_MOVE_DISTANCE  # Current speed of all cars

    def create_car(self):
        """
        Randomly creates a new car with a 1/6 chance each time it's called.
        Cars are created at the right edge of the screen with random colors and positions.
        """
        random_chance = random.randint(1, 6)  # Generate random number 1-6
        if random_chance == 1:  # Only create car if random number is 1 (1/6 chance)
            # Create new car turtle
            new_car = Turtle("square")  # Use square shape for car
            new_car.shapesize(stretch_wid=1, stretch_len=2)  # Make car rectangular (1x2)
            new_car.penup()  # Don't draw lines when moving
            new_car.color(random.choice(COLORS))  # Assign random color from COLORS list
            
            # Position car at random height on right edge of screen
            random_y = random.randint(-250, 250)  # Random Y position within screen bounds
            new_car.goto(300, random_y)  # Place car at right edge (x=300)
            
            # Add new car to the list of all cars
            self.all_cars.append(new_car)

    def move_cars(self):
        """
        Move all existing cars to the left by the current car speed.
        """
        for car in self.all_cars:
            car.backward(self.car_speed)  # Move car left by car_speed pixels

    def level_up(self):
        """
        Increase the speed of all cars when player advances to next level.
        """
        self.car_speed += MOVE_INCREMENT  # Increase speed by MOVE_INCREMENT
