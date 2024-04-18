from tkinter import *
from tkinter import ttk
import tkinter as tk
import numpy as np
import random
import math

class gameBoard:
    size = 0
    tiles = []
    def __init__(self, scale):
        self.size = scale
        #print(self.size)

class snake:
    length = 4
    positionX = 0
    positionY = 0
    dX = 0
    dY = 0
    positionsX = []
    positionsY = []

    def move(self, directionX, directionY):
        self.dX = directionX
        self.dY = directionY

    def draw(self, board, canvas, apple):
        canvas.delete("square")  # Clear previous square
        
        if len(self.positionsX) >= self.length: # remove the oldest saved positons
            self.positionsX.pop(0)
            self.positionsY.pop(0)
        
        self.positionsX.append(self.positionX) # save the current position
        self.positionsY.append(self.positionY)

        if self.positionX + self.dX < (500 / board.size) and self.positionX + self.dX >= 0: # update the position
            self.positionX += self.dX
        else:
            pass # call kill player
        if self.positionY + self.dY < (500 / board.size) and self.positionY + self.dY >= 0:
            self.positionY += self.dY
        else:
            pass # call kill player
        
        counter = 0
        for pos in self.positionsX: # make sure we cant enter a tail
            if self.positionX == self.positionsX[counter] or self.positionY == self.positionsY[counter]:
                pass # call kill player
        

        if self.positionX == apple.positionX and self.positionY == apple.positionY:
            apple.MoveSpot(board)
            self.length += 1

        canvas.create_rectangle(self.positionX * board.size, self.positionY * board.size, self.positionX * board.size + board.size, self.positionY * board.size + board.size, fill="green", tags="square") # draw the snake in the new position

        counter = 0
        for pos in self.positionsX: # draw the remaining segments
            canvas.create_rectangle(self.positionsX[counter] * board.size, self.positionsY[counter] * board.size, self.positionsX[counter] * board.size + board.size, self.positionsY[counter] * board.size + board.size, fill="green", tags="square")
            counter += 1

        form.after(100, lambda: self.draw(board, canvas, apple)) # repeat every 100ms

class food:
    positionX = 0
    positionY = 0

    def MoveSpot(self, board):
        self.positionX = math.trunc(random.random() * board.size)
        self.positionY = math.trunc(random.random() * board.size)
        pass

    def draw(self, board, canvas):
        canvas.delete("food")
        canvas.create_rectangle(self.positionX * board.size, self.positionY * board.size, self.positionX * board.size + board.size, self.positionY * board.size + board.size, fill="red", tags="food")
        form.after(100, lambda: self.draw(board, canvas))


player = snake()
board = gameBoard(20)
apple = food()

def onKeyPress(event):
    match event.keysym:
        case "w":
            player.move(0,-1)
            pass
        case "a":
            player.move(-1, 0)
            pass
        case "s":
            player.move(0, 1)
            pass
        case "d":
            player.move(1, 0)
            pass
        case "Escape":
            form.quit()
            pass
    #print(event.keysym)
    pass

form = Tk()
form.title('Snake.py')
form.geometry('500x500')
form.configure(background='black')
canvas = tk.Canvas(form, width=500, height=500, bg='black')
canvas.pack()
form.bind('<KeyPress>', onKeyPress)

apple.MoveSpot(board)

player.draw(board, canvas, apple)
apple.draw(board, canvas)

form.mainloop()