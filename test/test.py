from tkinter import *
import random
rows = 3
cols = 3
    
def buttonClick():
    if(btn == None):
        print('')

root = Tk()

arr = [[0 for _ in range(rows)] for _ in range(cols)]
num = random.sample(range(1,rows*cols+1),rows*cols)
k = 0

num[num.index(rows*cols)] = None

for i in range(rows):
    for j in range(cols):
        arr[i][j] = num[k]
        btn = Button(root, text=arr[i][j], width=20, height=9, command=buttonClick).grid(row=i, column=j)
        k += 1

root.mainloop()