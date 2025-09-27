# Import necessary modules
from turtle import Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# === GAME SETUP ===
# Create and configure the game screen
screen = Screen()
screen.setup(width=600, height=600)  # Set screen dimensions
screen.tracer(0)  # Turn off animation for smoother gameplay

# Initialize game objects
scoreboard = Scoreboard()  # Create scoreboard to track level and display game over
car_manager = CarManager()  # Create car manager to handle car creation and movement
player = Player()  # Create the player turtle

# === CONTROLS ===
# Set up keyboard controls
screen.listen()  # Enable the screen to listen for key presses
screen.onkey(player.move_up, "Up")  # Bind Up arrow key to move player up

# === MAIN GAME LOOP ===
game_on = True  # Game state flag
while game_on:
    time.sleep(0.1)  # Control game speed (pause for 0.1 seconds each frame)
    screen.update()  # Refresh the screen to show updates
    
    # Car management
    car_manager.create_car()  # Randomly create new cars
    car_manager.move_cars()   # Move all existing cars across the screen
    
    # === COLLISION DETECTION ===
    # Check if player collides with any car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:  # If player is within 20 units of a car
            game_on = False  # End the game
            scoreboard.game_over()  # Display game over message
    
    # === LEVEL PROGRESSION ===
    # Check if player successfully crossed to the other side
    if player.crossed_success():
        player.go_to_start()        # Reset player position to starting point
        car_manager.level_up()      # Increase car speed for next level
        scoreboard.increase_level() # Update and display new level

# Keep the screen open until clicked
screen.exitonclick()
