
import tkinter as tk
def create_button_grid(master, rows, cols, width, height):
    button_width = width // cols  # 각 버튼의 너비
    button_height = height // rows  # 각 버튼의 높이

    for i in range(rows):
        for j in range(cols):
            button = tk.Button(master, text=f"{i*cols + j + 1}", width=button_width, height=button_height)
            button.grid(row=i, column=j, sticky="nsew") # sticky로 모든 방향에 붙임
   
    button = tk.Button(master, text="", width=button_width, height=button_height)
    button.grid(row=2, column=2, sticky="nsew")
    
root = tk.Tk()
root.geometry("500x500")
# # 가중치 설정으로 버튼들이 공간을 균일하게 차지하도록 함
for i in range(3):
    root.rowconfigure(i, weight=1)
    root.columnconfigure(i, weight=1)
# 3x3 버튼 그리드 생성
create_button_grid(root, 3, 3, 500, 500)
root.mainloop()
