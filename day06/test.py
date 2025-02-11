from tkinter import *
import random
rows = 3
cols = 3
arr = [[0 for _ in range(rows)] for _ in range(cols)]
num = random.sample(range(1,rows*cols+1),rows*cols)
k = 0

def buttonClick():
    for i in range(rows):
        for j in range(cols):
            if(arr[i][j] == None):
                arr[i][j] = arr[i][j+1]
                arr[i][j+1] = None


root = Tk()

num[num.index(rows*cols)] = None

for i in range(rows):
    for j in range(cols):
        arr[i][j] = num[k]
        Button(root, text=arr[i][j], width=20, height=9, command=buttonClick).grid(row=i, column=j)
        k += 1

root.mainloop()

# [ , 2, 3]
# [4, 5, 6]
# [7, 8, 9]