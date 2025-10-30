import turtle as trtl
import random as rand

myPen = trtl.Screen()
myPen.bgcolor("black")
myPen.title("Turtle Boss Fight")

# --- Game Setup ---
myPen.addshape("wizard.gif")  # Add a custom shape for the player
myPen.addshape("monster.gif") # Add a custom shape for the boss
myPen.bgpic("Backgrounda.gif")
# Create the player turtle
player = trtl.Turtle()
player.shape("wizard.gif")
player.penup()
player.goto(-200, 0)
player_health = 100

# Create the boss turtle
boss = trtl.Turtle()
boss.shape("monster.gif")
boss.penup()
boss.goto(200, 0)
boss_health = 200

# Create a writer turtle for game messages
writer = trtl.Turtle()
writer.color("hot pink")
writer.penup()
writer.hideturtle()
writer.goto(0, 250)

# Create a turtle to display health bars

# Game state variables

# --- Reset Function ---

   

    # Clear screen and update visuals

    # Enable key bindings for the game

    # Display play again option
    
# --- 1st Option ---

# --- 2nd Option ---

# --- 3rd option ---

# --- Key bindings and start ---

# Start the game


myPen.mainloop()