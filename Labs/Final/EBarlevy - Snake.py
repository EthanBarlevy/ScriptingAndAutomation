from tkinter import *
from tkinter import ttk
import numpy as np
import vector

class gameBoard:
    size = 0
    tiles = []
    def __init__(self, scale):
        self.size = scale

class snake:
    length = 4
    position = vector.Vector2D(x=0, y=0)
    positions = []

    def move(direction):
        if(position.x + direction.x > 0 and
           position.x + direction.x < board.size and
           position.y + direction.y > 0 and
           position.y + direction.y < board.size):
            position += direction
        print(position)



player = snake()
board = gameBoard(20)

def onKeyPress(event):
    match event.keysym:
        case "w":
            player.move(vector.Vector2D(x=0, y=-1))
            pass
        case "a":
            player.move(vector.Vector2D(x=-1, y=0))
            pass
        case "s":
            player.move(vector.Vector2D(x=0, y=1))
            pass
        case "d":
            player.move(vector.Vector2D(x=-1, y=0))
            pass
        case "Escape":
            form.quit()
            pass
    print(event.keysym)
    pass

form = Tk()
form.title('Snake.py')
form.geometry('500x500')
form.configure(background='black')
form.bind('<KeyPress>', onKeyPress)

form.mainloop()