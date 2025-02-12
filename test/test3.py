from tkinter import *
import random
from tkinter import messagebox

class Puzzle(Tk):
    def __init__(self):
        super().__init__()
        self.title('슬라이드 퍼즐')
        self.rows = 4
        self.cols = 4
        self.arr = [[None for _ in range(self.rows)] for _ in range(self.cols)]
        self.empty_button = None
        self.buttons = [[None for _ in range(self.cols)] for _ in range(self.rows)]
        
        self.shuffle_puzzle()
        self.create_button()

    def button_click(self, i, j):
        if self.arr[i][j] is None: # 빈칸을 클릭하면 성공 메시지
            if self.check_success():
                messagebox.showinfo('성공', '성공') 
        elif (abs(i - self.empty_button[0]) == 1 and j == self.empty_button[1]) or (abs(j - self.empty_button[1]) == 1 and i == self.empty_button[0]):
            self.arr[self.empty_button[0]][self.empty_button[1]], self.arr[i][j] = self.arr[i][j], self.arr[self.empty_button[0]][self.empty_button[1]]
            self.empty_button = (i, j)
            self.update_button_text()

    def create_button(self):
        for i in range(self.rows):
            for j in range(self.cols):
                button_text = self.arr[i][j] if self.arr[i][j] is not None else ''
                button = Button(self, text=button_text, width=5, height=2, font=('Arial', 40),
                               command=lambda i=i, j=j: self.button_click(i, j))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button  # 버튼을 리스트에 저장

    def update_button_text(self):
        for i in range(self.rows):
            for j in range(self.cols):
                button_text = self.arr[i][j] if self.arr[i][j] is not None else ''
                self.buttons[i][j].config(text=button_text)  # 버튼 텍스트 변경

    def shuffle_puzzle(self):
        num = random.sample(range(1, self.rows * self.cols), self.rows * self.cols - 1)
        num.append(None)
        random.shuffle(num)

        k = 0
        for i in range(self.rows):
            for j in range(self.cols):
                self.arr[i][j] = num[k]
                if num[k] is None:
                    self.empty_button = (i, j)
                k += 1

    def check_success(self):
        correct_arr = [i for i in range(1, self.rows * self.cols)] + [None]
        flat_arr = [self.arr[i][j] for i in range(self.rows) for j in range(self.cols)]
        return flat_arr == correct_arr  # 성공했으면 True, 아니면 False 반환


if __name__ == '__main__':
    app = Puzzle()
    app.mainloop()
