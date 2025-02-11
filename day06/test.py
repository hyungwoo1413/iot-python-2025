from tkinter import *
import random

def makeButton():
    rows = 3
    cols = 3
    arr = [[0 for _ in range(rows)] for _ in range(cols)]
    num = random.sample(range(1,rows*cols+1),rows*cols)
    k = 0

    num[num.index(rows*cols)] = None

    for i in range(rows):
        for j in range(cols):
            arr[i][j] = num[k]
            Button(root, text=arr[i][j], width=20, height=9).grid(row=i, column=j)
            k += 1
    return arr

def buttonClick():
    pass



root = Tk()
arr = makeButton()

if(arr[0][0] == None):
    if(buttonClick()):
        pass

root.mainloop()

# [ , 2, 3]
# [4, 5, 6]
# [7, 8, 9]