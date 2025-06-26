import random
import turtle
import tkinter as tk

win = turtle.Screen()
win.title("Squid Game")

win.bgcolor("#9a4d74")
win.setup(width = 800, height = 800)
win.tracer(0)

canvas = win.getcanvas()
tk_window = canvas.winfo_toplevel()

player = None
enemies = []
gameOver = False


pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.color = "white"


waves = 0

logo_label = None
logo_name_label = None

# Game Title
logo_title = tk.PhotoImage(file = "images/Squid-Game.png") 
logo_name = tk.PhotoImage(file = "images/Attack-of-the-shapes.png")

# Move the character up
def player_up():
    y = player.ycor()
    y += 20
    player.sety(y)

# Move the character down
def player_down():
    y = player.ycor()
    y -= 20
    player.sety(y)

# Move the character left
def player_left():
    x = player.xcor()
    x -= 20
    player.setx(x)

# Move the character right
def player_right():
    x = player.xcor()
    x += 20
    player.setx(x)

# If the player resets the game
def reset_game():
    global gameOver, waves
    pen.clear()
    gameOver = False
    for enemy in enemies:
        enemy.clear()
        enemy.dy = 1
        enemy.goto(random.randint(-380, 380), 400)
        enemy.showturtle()
        
    player.goto(0,0)
    player.showturtle()
    game_loop()


# When clicking start button, starts the game
def start_game():
    global start_button, how_to_play_button
    global player, enemies, waves, gameOver, pen
    global logo_label, logo_name_label

    if logo_label is not None:
        logo_label.destroy()
    if logo_name_label is not None:
        logo_name_label.destroy()
    
    start_button.destroy()
    how_to_play_button.destroy()

    win.bgcolor("#9a4d74")
    win.tracer(0)

    sprite = "images/sg-sprite.gif"
    win.addshape(sprite)

    # loads the sprite
    player = turtle.Turtle() 
    player.shape(sprite)
    player.penup()
    player.goto(0, 0)
    player.showturtle()

    # Enemy 1: Triangle
    enemy1 = turtle.Turtle()
    enemy1.speed(0)
    enemy1.shape("triangle")
    enemy1.color("grey")
    enemy1.shapesize(stretch_wid=7, stretch_len= 7)
    enemy1.penup()
    enemy1Start = random.randint(-int(win.window_width() / 2), int(win.window_width() / 2))
    enemy1.goto(enemy1Start, (win.window_height() / 2 + 250))
    enemy1.dy = 1
    enemy1.showturtle()

    # Enemy 2: Circle
    enemy2 = turtle.Turtle()
    enemy2.speed(0)
    enemy2.shape("circle")
    enemy2.color("grey")
    enemy2.shapesize(stretch_wid=7, stretch_len= 7)
    enemy2.penup()
    enemy2Start = random.randint(-int(win.window_width() / 2), int(win.window_width() / 2))
    enemy2.goto(enemy2Start, (win.window_height() / 2 + 250))
    enemy2.dy = 1
    enemy2.showturtle()

    # Enemy 3: Square
    enemy3 = turtle.Turtle()
    enemy3.speed(0)
    enemy3.shape("square")
    enemy3.color("grey")
    enemy3.shapesize(stretch_wid=7, stretch_len= 7)
    enemy3.penup()
    enemy3Start = random.randint(-int(win.window_width() / 2), int(win.window_width() / 2))
    enemy3.goto(enemy3Start, (win.window_height() / 2 + 250))
    enemy3.dy = 1
    enemy3.showturtle()

    # Enemy 4: Arrow
    enemy4 = turtle.Turtle()
    enemy4.speed(0)
    enemy4.shape("arrow")
    enemy4.color("grey")
    enemy4.shapesize(stretch_wid=7, stretch_len= 7)
    enemy4.penup()
    enemy4Start = random.randint(-int(win.window_width() / 2), int(win.window_width() / 2))
    enemy4.goto(enemy4Start, (win.window_height() / 2 + 250))
    enemy4.dy = 1
    enemy4.showturtle()

    gameOver = False
    waves = 0

    # Listens for keyboard commands
    win.listen()
    win.onkeypress(player_up, "Up")
    win.onkeypress(player_down, "Down")
    win.onkeypress(player_left, "Left")
    win.onkeypress(player_right, "Right")

    global enemies
    enemies = [enemy1, enemy2, enemy3, enemy4]


    game_loop()



def game_loop():
    global waves, gameOver
    if not gameOver:
        # Boundaries set for X and Y
        if player.ycor() > 300:
            player.sety(300)

        if player.ycor() < -300:
            player.sety(-300)

        if player.xcor() > 380:
            player.setx(380)

        if player.xcor() < -380:
            player.setx(-380)
        
        for enemy in enemies:
            enemy.sety(enemy.ycor() - enemy.dy)
            if enemy.ycor() < -450:
                new_x = random.randint(-int(win.window_width() / 2), int(win.window_width() / 2))
                enemy.goto(new_x, (win.window_height() / 2 + 250))
                enemy.dy += 0.5 # Increases the speed
                waves += 1 # Wave counter to track # of times
            if enemy.dy > 10: 
                enemy.dy = 10 # Cap the speed increase at 10, if they survive that long lol

        for enemy in enemies:
            # If the enemy touches player
            if (enemy.ycor() <= player.ycor() + 60 and enemy.xcor() < player.xcor() + 20 and enemy.xcor() > player.xcor() - 20
            and enemy.ycor() >= player.ycor()): 
                gameOver = True
        pen.clear()
        pen.goto(-380, 350)
        pen.write(f"Waves: {waves}", align="left", font=("Courier", 18, "bold"))
        win.ontimer(game_loop, 20)
        win.update()
    
    else:
   
        for enemy in enemies:
            enemy.dy = 0
            enemy.hideturtle()

        player.hideturtle()
        pen.goto(0, 25)
        pen.write(f"Game Over... You survived {waves} waves.", align = "center", font = ("Courier", 35, "normal"))
        pen.goto(0, -25)
        pen.write("Press return to restart.", align= "center", font = ("Courier", 25, "normal"))
        win.onkeypress(reset_game, "Return")
    
# How To Play Screen
def how_to_play():
    start_button.destroy()
    how_to_play_button.destroy()
    global logo_label, logo_name_label
    if logo_label is not None:
        logo_label.destroy()
    if logo_name_label is not None:
        logo_name_label.destroy()
    
    pen.clear()
    pen.goto(0, 100)
    pen.write("Attack of the Shapes!\nIn a turn of events, the masked-men are now playing the Squid Games\n\n\nAvoid falling enemies\nUse the Arrow keys to move around\nIf you touch any obstacles, the game over.", align = "center", font = ("Courier", 18, "bold"))

    global back_button
    back_button = tk.Button(tk_window, text = "Back", font = ("Courier", 35), bg = "white", command = go_back_to_home)
    back_button.place(x = 340, y = 600)

# Go Back to Home Screen
def go_back_to_home():
    pen.clear()
    back_button.destroy()


    global start_button, how_to_play_button
    global logo_label, logo_name_label

    if logo_label is not None:
        logo_label.destroy()
    if logo_name_label is not None:
        logo_name_label.destroy()

    how_to_play_button= tk.Button(tk_window, text = "How To Play", command = how_to_play, font = ("Courier", 35), bg = "white")
    how_to_play_button.place(x = 275, y = 350)
    start_button = tk.Button(tk_window, text = "Start Game", command = start_game, font = ("Courier", 35), bg = "white")
    start_button.place(x = 275, y = 425)

    logo_name_label = tk.Label(tk_window, image = logo_name, bg = "#9a4d74")
    logo_name_label.place(x = 150, y = 250)

    logo_label = tk.Label(tk_window, image = logo_title, bg = "#9a4d74")
    logo_label.place(x = 225, y = 150)


# Main Screen

logo_name_label = tk.Label(tk_window, image = logo_name, bg = "#9a4d74")
logo_name_label.place(x = 150, y = 250)

logo_label = tk.Label(tk_window, image = logo_title, bg = "#9a4d74")
logo_label.place(x = 225, y = 150)


how_to_play_button= tk.Button(tk_window, text = "How To Play", command = how_to_play, font = ("Courier", 35), bg = "white")
how_to_play_button.pack()
how_to_play_button.place(x = 250, y = 350)

start_button = tk.Button(tk_window, text = "Start Game", command = start_game, font = ("Courier", 35), bg = "white")
start_button.pack()
start_button.place(x = 250, y = 425)
    






win.mainloop()





