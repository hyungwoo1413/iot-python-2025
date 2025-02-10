from tkinter import *
import tkinter.font as fnt

root = Tk()
root.geometry('400x200')
root.title('카운트 예제') # 윈도우 창 제목변경

# 이벤트
count = 0 # 계속 증가시킬 수를 담는 변수

def countUp():
    global count # 전역변수 count를 함수내에서 사용할 거야!
    count += 1
    label['text'] = f'버튼클릭: {count}' # 라벨에 표시

def countInit():
    global count
    count = 0
    label['text'] = f'버튼클릭: {count}'

myfont = fnt.Font(family='NanumGothic', size=20)

# 라벨(숫자카운트를 표시)
label = Label(root, text=f'버튼클릭: {count}', fg='blue', font=myfont)
# side = LEFT, TOP, RIGHT, BOTTOM
# padding = 안쪽 여백, padx(왼쪽, 오른쪽 여백), pady(위, 아래 여백)
label.pack(side=TOP, pady=20)
# 버튼, command 파라미터: 이벤트 함수를 정의
buttonUp = Button(root, text='카운트 증가', font=myfont, command=countUp) # countUp 이라는 함수가 마우스 클릭할때마다 실행
buttonUp.pack(side=LEFT, padx=20, pady=20)
buttonInit = Button(root, text='초기화', font=myfont, command=countInit)
buttonInit.pack(side=RIGHT, padx=20, pady=20)

root.mainloop()