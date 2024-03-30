# Day 53: Create a program that allows users to draw on a canvas using a GUI.
from tkinter import *
root = Tk()
canvas = Canvas(root, height=400, width=600, bg='white')
def draw(event):
    x, y = event.x, event.y
    canvas.create_oval(x-1, y-1, x+1, y+1, fill='black')
canvas.bind('<B1-Motion>', draw)
canvas.pack()
mainloop()
