from tkinter import *
from tkinter import messagebox
import random

rows = 4
cols = 4
arr = [[None for _ in range(rows)] for _ in range(cols)]
empty_button = None

def buttonClick(i, j):
    global empty_button

    if (abs(i - empty_button[0]) == 1 and j == empty_button[1]) or (abs(j - empty_button[1]) == 1 and i == empty_button[0]):
        arr[empty_button[0]][empty_button[1]], arr[i][j] = arr[i][j], arr[empty_button[0]][empty_button[1]]
        empty_button = (i, j)
        update_button()
        check_success()

def update_button():
    for i in range(rows):
        for j in range(cols):
            button = Button(root, text=arr[i][j] if arr[i][j] is not None else "", 
                            width=5, height=3, font=("Arial",40), command=lambda i=i, j=j: buttonClick(i, j))
            button.grid(row=i, column=j)

def shuffle_puzzle():
    global empty_button
    num = random.sample(range(1, rows * cols), rows * cols - 1)

    num.append(None)
    random.shuffle(num)
    
    k = 0
    for i in range(rows):
        for j in range(cols):
            arr[i][j] = num[k]
            if num[k] is None:
                empty_button = (i, j)
            k += 1

def check_success():
    correct_arr = [i for i in range(1, rows * cols)] + [None]
    flat_arr = [arr[i][j] for i in range(rows) for j in range(cols)]
    
    if flat_arr == correct_arr:
        messagebox.showinfo("성공", "성공")


root = Tk()
root.title('슬라이드 퍼즐')
shuffle_puzzle()
update_button()
root.mainloop()
