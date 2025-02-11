from tkinter import *
import random

FWIDTH = 600
FHEIGHT = 600
RES = f'{FWIDTH}x{FHEIGHT}'
OWIDTH = 200
OHEIGHT = 200

class MyPuzzle(Tk):

    def __init__(self):
        super().__init__()
        self.settings()
        self.randomize()        # 숫자 섞기
        self.make_Button()      # 버튼 객체 생성
        self.set_Button()       # 버튼 객체 배치


    def settings(self):
        self.title('숫자 퍼즐')

    def randomize(self):
        self.randomList = [i for i in range(9)]
        random.shuffle(self.randomList)

    # 3x3 버튼 배열 삽입
    # 버튼의 text는 랜덤하게 배치되어야 함
    def make_Button(self):
        self.ButtonList = []
        for i in range(1,10):
            _button = Button(self, text=i, font=('Arial',72))
            _button.config(command=lambda b=_button: self.move_Object(b))
            self.ButtonList.append(_button)

    def set_Button(self):
        for idx,_button in enumerate(self.ButtonList):
            _col = self.randomList[idx] % 3
            _row = self.randomList[idx] // 3
            if _button.cget('text') == 9:
                _button.config(text='  ')
            _button.grid(row=_row,column=_col)

    def swap_elements(self,lst, index1, index2):
        lst[index1], lst[index2] = lst[index2], lst[index1]

    ## 무브 알고리즘 ㅅㅂ
    def move_Object(self,b):
        if b.cget('text') != '  ':
            clickedNum = int(b.cget('text'))            # 몇번이 눌렸냐
            bLindex = self.ButtonList.index(clickedNum) # 7번이 저장된 버튼리스트의 인덱스를 찾음
            index = self.randomList[bLindex]            # 매핑된 랜덤 리스트의 인덱스 값을 찾음
            LeftIndex = self.randomList.index(index-1)  # 선택된 곳의 왼쪽
            RightIndex = self.randomList.index(index+1) # 오른쪽
            UpIndex = self.randomList.index(index-3)    # 위쪽
            DownIndex = self.randomList.index(index+3)  # 아래쪽

            if index == 0 :
                if self.ButtonList[RightIndex].cget('text') == 9:
                    self.swap_elements(self.ButtonList,RightIndex,index)
                elif self.ButtonList[DownIndex].cget('text') == 9:
                    self.swap_elements(self.ButtonList,DownIndex,index)                
            if index == 1 :
                if self.ButtonList[LeftIndex].cget('text') == 9:
                    self.swap_elements(self.ButtonList,LeftIndex,index)
                elif self.ButtonList[DownIndex].cget('text') == 9:
                    self.swap_elements(self.ButtonList,DownIndex,index)                
                elif self.ButtonList[RightIndex].cget('text') == 9:
                    self.swap_elements(self.ButtonList,RightIndex,index)
            if index == 2 :
                if self.ButtonList[LeftIndex].cget('text') == 9:
                    self.swap_elements(self.ButtonList,LeftIndex,index)
                elif self.ButtonList[DownIndex].cget('text') == 9:
                    self.swap_elements(self.ButtonList,DownIndex,index)
                    

        self.set_Button()


#------------------------------

if __name__ == "__main__":
    app = MyPuzzle()
    app.mainloop()