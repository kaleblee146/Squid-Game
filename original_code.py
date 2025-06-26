import random
import turtle

win = turtle.Screen()
win.title("Squid Game")

win.bgcolor("#9a4d74")
win.setup(width = 800, height = 800)
win.tracer(0)

sprite = "images/sg-sprite.gif"
win.addshape(sprite)


player = turtle.Turtle()
player.shape(sprite)
player.penup()
player.goto(0, 0)

enemy1 = turtle.Turtle()
enemy1.speed(0)
enemy1.shape("triangle")
enemy1.color("grey")
enemy1.shapesize(stretch_wid=7, stretch_len= 7)
enemy1.penup()
enemy1Start = random.randint(-int(win.window_width() / 2), int(win.window_width() / 2))
enemy1.goto(enemy1Start, (win.window_height() / 2 + 250))
enemy1.dy = 1

enemy2 = turtle.Turtle()
enemy2.speed(0)
enemy2.shape("circle")
enemy2.color("grey")
enemy2.shapesize(stretch_wid=7, stretch_len= 7)
enemy2.penup()
enemy2Start = random.randint(-int(win.window_width() / 2), int(win.window_width() / 2))
enemy2.goto(enemy2Start, (win.window_height() / 2 + 250))
enemy2.dy = 1

enemy3 = turtle.Turtle()
enemy3.speed(0)
enemy3.shape("square")
enemy3.color("grey")
enemy3.shapesize(stretch_wid=7, stretch_len= 7)
enemy3.penup()
enemy3Start = random.randint(-int(win.window_width() / 2), int(win.window_width() / 2))
enemy3.goto(enemy3Start, (win.window_height() / 2 + 250))
enemy3.dy = 1

enemy4 = turtle.Turtle()
enemy4.speed(0)
enemy4.shape("arrow")
enemy4.color("grey")
enemy4.shapesize(stretch_wid=7, stretch_len= 7)
enemy4.penup()
enemy4Start = random.randint(-int(win.window_width() / 2), int(win.window_width() / 2))
enemy4.goto(enemy4Start, (win.window_height() / 2 + 250))
enemy4.dy = 1

gameOver = False
resetGame = False
waves = 0

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()

def player_up():
    y = player.ycor()
    y += 20
    player.sety(y)

def player_down():
    y = player.ycor()
    y -= 20
    player.sety(y)

def player_left():
    x = player.xcor()
    x -= 20
    player.setx(x)

def player_right():
    x = player.xcor()
    x += 20
    player.setx(x)

def set_false():
    return False

def leave_loop(x):
    x[0] = set_false()


win.listen()
win.onkeypress(player_up, "Up")
win.onkeypress(player_down, "Down")
win.onkeypress(player_left, "Left")
win.onkeypress(player_right, "Right")

while True:
    win.update()

    

    if player.ycor() > 300:
        player.sety(300)

    if player.ycor() < -300:
        player.sety(-300)

    if player.xcor() > 380:
        player.setx(380)

    if player.xcor() < -380:
        player.setx(-380)

    enemies = [enemy1, enemy2, enemy3, enemy4]
    for enemy in enemies:
        enemy.sety(enemy.ycor() - enemy.dy)
        if enemy.ycor() < -450:
            new_x = random.randint(-int(win.window_width() / 2), int(win.window_width() / 2))
            enemy.goto(new_x, (win.window_height() / 2 + 250))
            enemy.dy += 0.5
            waves += 1
        if enemy.dy > 10:
            enemy.dy = 10

    for enemy in enemies:
        if (enemy.ycor() <= player.ycor() + 60 and enemy.xcor() < player.xcor() + 20 and enemy.xcor() > player.xcor() - 20
        and enemy.ycor() >= player.ycor()):
            gameOver = True
        

    if gameOver:
        for enemy in enemies:
            enemy.dy = 0
            enemy.hideturtle()

        player.hideturtle()
        pen.goto(0, 25)
        pen.write(f"Game Over... You survived {waves} waves.", align = "center", font = ("Courier", 35, "normal"))
        pen.goto(0, -25)
        pen.write("Leave window to exit.", align= "center", font = ("Courier", 25, "normal"))
        resetGame = True
        gameOverArray = [gameOver]

        win.onkeypress(lambda: leave_loop(gameOverArray), "Return")
        gameOver = gameOverArray[0]

    if resetGame and not gameOver:
        pen.clear()
        player.showturtle()
        player.goto(0, 0)
        '''
        enemy1.dy = .2  
        enemy2.dy = .3
        enemy3.dy = .4
        enemy4.dy = .1
        '''
        

        enemy1Start = random.randint(-int(win.window_width() / 2), int(win.window_width() / 2))
        enemy2Start = random.randint(-int(win.window_width() / 2), int(win.window_width() / 2))
        enemy3Start = random.randint(-int(win.window_width() / 2), int(win.window_width() / 2))
        enemy4Start = random.randint(-int(win.window_width() / 2), int(win.window_width() / 2))

        enemy1.goto(enemy1Start, (win.window_height() / 2 + 250))
        enemy2.goto(enemy2Start, (win.window_height() / 2 + 250))
        enemy3.goto(enemy3Start, (win.window_height() / 2 + 250))
        enemy4.goto(enemy4Start, (win.window_height() / 2 + 250))

        resetGame = False

"""
    currentEnemy = random.randint(1,4)

    if currentEnemy == 1:
        enemy1.sety(enemy1.ycor() - enemy1.dy)
        if enemy1.ycor() < -450:
            enemy1Start = random.randint(-int(win.window_width() / 2), int(win.window_width() / 2))
            enemy1.goto(enemy1Start, (win.window_height() / 2 + 250))
            enemy1.dy += 1
    
    if currentEnemy == 2:
        enemy2.sety(enemy2.ycor() - enemy2.dy)
        if enemy2.ycor() < -450:
            enemy2Start = random.randint(-int(win.window_width() / 2), int(win.window_width() / 2))
            enemy2.goto(enemy2Start, (win.window_height() / 2 + 250))
            enemy2.dy += 1

    if currentEnemy == 3:
        enemy3.sety(enemy3.ycor() - enemy3.dy)
        if enemy3.ycor() < -450:
            enemy3Start = random.randint(-int(win.window_width() / 2), int(win.window_width() / 2))
            enemy3.goto(enemy3Start, (win.window_height() / 2 + 250))
            enemy3.dy += 1

    if currentEnemy == 4:
        enemy4.sety(enemy4.ycor() - enemy4.dy)
        if enemy4.ycor() < -450:
            enemy4Start = random.randint(-int(win.window_width() / 2), int(win.window_width() / 2))
            enemy4.goto(enemy4Start, (win.window_height() / 2 + 250))
            enemy4.dy += 1
"""

    

"""
    if (enemy1.ycor() <= player.ycor() + 60 and enemy1.xcor() < player.xcor() + 20 and enemy1.xcor() > player.xcor() - 20
        and enemy1.ycor() >= player.ycor()):
        gameOver = True

    if (enemy2.ycor() <= player.ycor() + 60 and enemy2.xcor() < player.xcor() + 20 and enemy2.xcor() > player.xcor() - 20
        and enemy2.ycor() >= player.ycor()):
        gameOver = True
    
    if (enemy3.ycor() <= player.ycor() + 60 and enemy3.xcor() < player.xcor() + 20 and enemy3.xcor() > player.xcor() - 20
        and enemy3.ycor() >= player.ycor()):
        gameOver = True

    if (enemy4.ycor() <= player.ycor() + 60 and enemy4.xcor() < player.xcor() + 20 and enemy4.xcor() > player.xcor() - 20
        and enemy4.ycor() >= player.ycor()):
        gameOver = True
"""










