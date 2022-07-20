import random
from tkinter import *
import threading
import time
# game grid
row1 = [0, 0, 0, 0]
row2 = [0, 0, 0, 0]
row3 = [0, 0, 0, 0]
row4 = [0, 0, 0, 0]
rows = [row1, row2, row3, row4]


class App(threading.Thread): # tkinter loop ran in a thread

    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

        
    def callback(self):
        self.root.quit()

    def run(self):
        # initial tkinter set up
        self.root = Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.callback)
        self.root.geometry("450x450")
        self.root.resizable(width=False, height=False)
        self.root.config(bg="#ADD8E6") # setting background colour
        

        self.root.bind("<Key>", keypress)
        time.sleep(1) # delay to mainloop so that other code can be set up to avoid errors
        self.root.mainloop()

    def labels(self):
        
        # code to draw the grid
        
        scale=6
        n=1

        for i in range(gridsize):
            r = rows[i]
            rn = i
            for i in range(gridsize):
                l = Label(self.root, text=str(r[i]), bg=returncolour(str(r[i])), width=2*scale, height=scale, borderwidth=n, relief="solid")
                l.grid(row=rn, column=i)

def returncolour(num): # tells the gui code what colour for each number
    if num == "0":
        return "#CCBBAA"
    if num == "2":
        return "#FFFFFF"
    if num == "4":
        return "#FFE5B4"
    if num == "8":
        return "#FFA500"
    return "#FFFFFF"

def keypress(event): # takes a tkinter keypress events, sends a call to the function for the direction of movement and tracks whether a move has been made to choose whether to add a new number
    print(event.char, event.keysym)
    temp = [list(row1), list(row2), list(row3), list(row4)]
    if event.char == "r" or event.keysym == "Right":
        moveRight()
    elif event.char == "l" or event.keysym == "Left":
        moveLeft()
    elif event.char == "u" or event.keysym == "Up":
        moveUp()
    elif event.char == "d" or event.keysym == "Down":
        moveDown()

    if temp[0] == rows[0] and temp[1] == rows[1] and temp[2] == rows[2] and temp[3] == rows[3]:
        print("no change")
    else:
        addrandom()
    app.labels()

def addrandom(): # adds either a 2 or a 4 square to an empty slot when a valid move has been made
    global rows
    numbers = [2, 2, 2, 2, 2, 2, 2, 2, 2, 4]
    num = random.choice(numbers)
    while True:
        rowIndex = random.randint(0,3)
        row = rows[rowIndex]
        if 0 in row:
            while True:
                n = random.randint(0,3)
                if row[n] == 0:
                    row[n] = num
                    break
                rows[rowIndex] = row
            break
        
def moveRight():
    for r in rows:
        for i in range(3):
            if r[i] == r[i+1]:
                r[i+1] = r[i] * 2
                r[i] = 0
            elif r[i+1] == 0:
                r[i+1] = r[i]
                r[i] = 0

def moveLeft():
    for r in rows:
        for i in range(3, 0, -1):
            if r[i] == r[i-1]:
                r[i-1] = r[i] * 2
                r[i] = 0
            elif r[i-1] == 0:
                r[i-1] = r[i]
                r[i] = 0

def moveDown():
    for i in range(3):
        r = rows[i]
        r2 = rows[i+1]
        for i in range(4):
            if r[i] == r2[i]:
                r2[i] = r[i] * 2
                r[i] = 0
            elif r2[i] == 0:
                r2[i] = r[i]
                r[i] = 0

def moveUp():
    for i in range(3, 0, -1):
        r = rows[i]
        r2 = rows[i-1]
        for i in range(4):
            if r[i] == r2[i]:
                r2[i] = r[i] * 2
                r[i] = 0
            elif r2[i] == 0:
                r2[i] = r[i]
                r[i] = 0

addrandom() # first square


app = App()
time.sleep(1) # delay to avoid errors with threading
app.labels() # first grid draw

