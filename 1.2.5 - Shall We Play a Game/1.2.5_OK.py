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
health_display = trtl.Turtle()
health_display.color("pink")
health_display.penup()
health_display.hideturtle()
health_display.goto(0, 220)
# Game state variables
is_player_turn = True
game_over = False
# --- Reset Function ---
def reset_game():
    """Resets the game to its initial state."""
    global player_health, boss_health, is_player_turn, game_over
    player_health = 100
    boss_health = 200
    is_player_turn = True
    game_over = False
    # Clear screen and update visuals
    writer.clear()
    health_display.clear()
    # Enable key bindings for the game
    myPen.onkeypress(use_magic_missile, "1")
    myPen.onkeypress(use_fireball, "2")
    myPen.onkeypress(use_heal, "3")
    update_health_display()
    show_options()
def update_health_display():
    """Draws and updates the health bars for the player and boss."""
    health_display.clear()
    health_display.write(
        f"Player Health: {player_health} | Boss Health: {boss_health}",
        align="center",
        font=("Arial", 16, "normal")
    )
def show_options():
    """Displays the player's choices on the screen."""
    writer.clear()
    writer.write(
        "Choose your action:\n"
        "1. Magic Missile (15 damage)\n"
        "2. Fireball (30 damage)\n"
        "3. Heal (20 health)",
        align="center",
        font=("Arial", 16, "normal")
    )
def player_attack(damage, choice_text):
    """Player's turn to attack."""
    global boss_health, is_player_turn
    if not is_player_turn or game_over:
        return
    writer.clear()
    writer.write(f"You used {choice_text}! The boss takes {damage} damage.", align="center", font=("Arial", 16, "normal"))
    boss_health -= damage
    update_health_display()
    if boss_health <= 0:
        end_game("player")
    else:
        is_player_turn = False
        myPen.ontimer(boss_turn, 2000) # Wait 2 seconds before boss attacks
def player_heal():
    """Player's turn to heal."""
    global player_health, is_player_turn
    if not is_player_turn or game_over:
        return
    heal_amount = 20
    writer.clear()
    writer.write(f"You heal yourself for {heal_amount} health.", align="center", font=("Arial", 16, "normal"))
    player_health += heal_amount
    update_health_display()
    is_player_turn = False
    myPen.ontimer(boss_turn, 2000)
def boss_turn():
    """The boss's turn to attack the player."""
    global player_health, is_player_turn
    if game_over:
        return
    writer.clear()
    boss_attack_type = rand.choice(["smash", "punch"])
    damage = rand.randint(10, 25)
    writer.write(f"The boss uses a {boss_attack_type}! You take {damage} damage.", align="center", font=("Arial", 16, "normal"))
    player_health -= damage
    update_health_display()
    if player_health <= 0:
        end_game("boss")
    else:
        is_player_turn = True
        myPen.ontimer(show_options, 2000) # Wait 2 seconds to show options again
def end_game(winner):
    """Ends the game and declares the winner."""
    global game_over
    game_over = True
    writer.clear()
    if winner == "player":
        writer.write("Congratulations, you defeated the boss!", align="center", font=("Arial", 24, "bold"))
    else:
        writer.write("Game Over! The boss has defeated you.", align="center", font=("Arial", 24, "bold"))
    # Display play again option
    writer.goto(0, 200)
    writer.write("Press 'r' to play again", align="center", font=("Arial", 16, "normal"))
    # Disable game keys and bind "r" to restart
    myPen.onkeypress(None, "1")
    myPen.onkeypress(None, "2")
    myPen.onkeypress(None, "3")
    myPen.onkeypress(reset_game, "r")
# --- 1st Option ---
def use_magic_missile():
    player_attack(15, "Magic Missile")
# --- 2nd Option ---
def use_fireball():
    player_attack(30, "Fireball")
# --- 3rd option ---
def use_heal():
    player_heal()
# --- Key bindings and start ---
myPen.listen()
myPen.onkeypress(use_magic_missile, "1")
myPen.onkeypress(use_fireball, "2")
myPen.onkeypress(use_heal, "3")
# Start the game
update_health_display()
show_options()
myPen.mainloop()