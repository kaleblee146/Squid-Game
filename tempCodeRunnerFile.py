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
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.color = "white"


game_started = [False]
game_over = False
reset_game = False


def start_game():
    start_button.destroy()
    how_to_play_button.destroy()
    game_started[0] = True


def how_to_play():
    start_button.destroy()
    how_to_play_button.destroy()
    logo_label.destroy()
    logo_name_label.destroy()
    pen.clear()
    pen.goto(0, 100)
    pen.write("Attack of the Shapes!\nIn a turn of events, the masked-men are now playing the Squid Games\n\n\nAvoid falling enemies\nUse the Arrow keys to move around\nIf you touch any obstacles, the game over.", align = "center", font = ("Courier", 18, "bold"))

    global back_button
    back_button = tk.Button(tk_window, text = "Back", font = ("Courier", 35), bg = "white", command = go_back_to_home)
    back_button.place(x = 340, y = 600)

def go_back_to_home():
    pen.clear()
    back_button.destroy()


    global start_button, how_to_play_button, logo_label, logo_name_label

    how_to_play_button= tk.Button(tk_window, text = "How To Play", command = how_to_play, font = ("Courier", 35), bg = "white")
    how_to_play_button.place(x = 275, y = 350)
    start_button = tk.Button(tk_window, text = "Start Game", command = start_game, font = ("Courier", 35), bg = "white")
    start_button.place(x = 275, y = 425)
    logo_title = tk.PhotoImage(file = "images/Squid-Game.png")
    logo_label = tk.Label(tk_window, image = logo_title, bg = "#9a4d74")
    logo_label.place(x = 225, y = 150)
    logo_name = tk.PhotoImage(file = "images/Attack-of-the-shapes.png")
    logo_name_label = tk.Label(tk_window, image = logo_name, bg = "#9a4d74")
    logo_name_label.place(x = 150, y = 250)

logo_name = tk.PhotoImage(file = "images/Attack-of-the-shapes.png")
logo_name_label = tk.Label(tk_window, image = logo_name, bg = "#9a4d74")
logo_name_label.place(x = 150, y = 250)

logo_title = tk.PhotoImage(file = "images/Squid-Game.png")
logo_label = tk.Label(tk_window, image = logo_title, bg = "#9a4d74")
logo_label.place(x = 225, y = 150)

logo_name = tk.PhotoImage(file = "images/Attack-of-the-shapes.png")
logo_name_label = tk.Label(tk_window, image = logo_name, bg = "#9a4d74")
logo_name_label.place(x = 150, y = 250)

how_to_play_button= tk.Button(tk_window, text = "How To Play", command = how_to_play, font = ("Courier", 35), bg = "white")
how_to_play_button.pack()
how_to_play_button.place(x = 250, y = 350)

start_button = tk.Button(tk_window, text = "Start Game", command = start_game, font = ("Courier", 35), bg = "white")
start_button.pack()
start_button.place(x = 250, y = 425)




win.mainloop()





