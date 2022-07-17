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
        self.root = Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.callback)
        self.root.geometry("450x450")
        self.root.resizable(width=False, height=False)
        self.root.config(bg="#ADD8E6")
        
        # gui code
        
        row1g = Label(self.root, text=str(row1))
        row2g = Label(self.root, text=str(row2))
        row3g = Label(self.root, text=str(row3))
        row4g = Label(self.root, text=str(row4))


        self.root.bind("<Key>", keypress)
        time.sleep(1)
        self.root.mainloop()

    def labels(self):

        scale=6
        n=1
        r0c0 = Label(self.root, text=str(row1[0]), bg=returncolour(str(row1[0])), width=2*scale, height=scale, borderwidth=n, relief="solid")
        r0c1 = Label(self.root, text=str(row1[1]), bg=returncolour(str(row1[1])), width=2*scale, height=scale, borderwidth=n, relief="solid")
        r0c2 = Label(self.root, text=str(row1[2]), bg=returncolour(str(row1[2])), width=2*scale, height=scale, borderwidth=n, relief="solid")
        r0c3 = Label(self.root, text=str(row1[3]), bg=returncolour(str(row1[3])), width=2*scale, height=scale, borderwidth=n, relief="solid")

        r1c0 = Label(self.root, text=str(row2[0]), bg=returncolour(str(row2[0])), width=2*scale, height=scale, borderwidth=n, relief="solid")
        r1c1 = Label(self.root, text=str(row2[1]), bg=returncolour(str(row2[1])), width=2*scale, height=scale, borderwidth=n, relief="solid")
        r1c2 = Label(self.root, text=str(row2[2]), bg=returncolour(str(row2[2])), width=2*scale, height=scale, borderwidth=n, relief="solid")
        r1c3 = Label(self.root, text=str(row2[3]), bg=returncolour(str(row2[3])), width=2*scale, height=scale, borderwidth=n, relief="solid")

        r2c0 = Label(self.root, text=str(row3[0]), bg=returncolour(str(row3[0])), width=2*scale, height=scale, borderwidth=n, relief="solid")
        r2c1 = Label(self.root, text=str(row3[1]), bg=returncolour(str(row3[1])), width=2*scale, height=scale, borderwidth=n, relief="solid")
        r2c2 = Label(self.root, text=str(row3[2]), bg=returncolour(str(row3[2])), width=2*scale, height=scale, borderwidth=n, relief="solid")
        r2c3 = Label(self.root, text=str(row3[3]), bg=returncolour(str(row3[3])), width=2*scale, height=scale, borderwidth=n, relief="solid")

        r3c0 = Label(self.root, text=str(row4[0]), bg=returncolour(str(row4[0])), width=2*scale, height=scale, borderwidth=n, relief="solid")
        r3c1 = Label(self.root, text=str(row4[1]), bg=returncolour(str(row4[1])), width=2*scale, height=scale, borderwidth=n, relief="solid")
        r3c2 = Label(self.root, text=str(row4[2]), bg=returncolour(str(row4[2])), width=2*scale, height=scale, borderwidth=n, relief="solid")
        r3c3 = Label(self.root, text=str(row4[3]), bg=returncolour(str(row4[3])), width=2*scale, height=scale, borderwidth=n, relief="solid")

        r0c0.grid(row=0,column=0)
        r0c1.grid(row=0, column=1)
        r0c2.grid(row=0, column=2)
        r0c3.grid(row=0, column=3)

        r1c0.grid(row=1,column=0)
        r1c1.grid(row=1, column=1)
        r1c2.grid(row=1, column=2)
        r1c3.grid(row=1, column=3)

        r2c0.grid(row=2,column=0)
        r2c1.grid(row=2, column=1)
        r2c2.grid(row=2, column=2)
        r2c3.grid(row=2, column=3)

        r3c0.grid(row=3,column=0)
        r3c1.grid(row=3, column=1)
        r3c2.grid(row=3, column=2)
        r3c3.grid(row=3, column=3)

def returncolour(num):
    if num == "0":
        return "#CCBBAA"
    if num == "2":
        return "#FFFFFF"
    if num == "4":
        return "#FFE5B4"
    if num == "8":
        return "#FFA500"
    return "#FFFFFF"

def printgrid(event):
    print(row1)
    print(row2)
    print(row3)
    print(row4)
    print("\n")

def keypress(event):
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

def addrandom(): # adds either a 2 or a 4 square to an empty slot when a valid move made
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

addrandom()


app = App()
time.sleep(1)
app.labels()



##while True:# main game loop
##    inp = input()

##    print(temp)
##    if inp == "u":
##        moveUp()
##    elif inp == "d":
##        moveDown()
##    elif inp == "l":
##        moveLeft()
##    elif inp == "r":
##        moveRight()
##    elif inp == "0":
##        break
##    print(rows)
##    app.labels()


    


    
            
        


    

