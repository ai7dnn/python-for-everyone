#%% 10-06convertfah.py	 버튼 이벤트 처리로 섭씨 온도를 화씨 온도로 변환
from tkinter import *

def fahrenhite(celsius):
    return celsius * 9 / 5 + 32

def clicked():
    degree = eval(cel.get()) #엔트리 cel에서 값 가져오기
    print(degree) #디버깅을 위해 출력
    fah.delete(0, END) #이전의 자료를 비우고
    fah.insert(0, str(fahrenhite(degree))) #새로 변환된 자료를 쓰고

win = Tk()
win.title('섭씨온도를 화씨온도로 변환')
 
lbcel = Label(win, text="섭씨 온도", width=10)
lbfar = Label(win, text="화씨 온도")
lbcel.grid(row=0, column=0)
lbfar.grid(row=1, column=0)

cel = Entry(win, width=20)
fah = Entry(win)
cel.grid(row=0, column=1)
fah.grid(row=1, column=1)

cvt = Button(win, text="변환", width=20, command = clicked)
cvt.grid(row=2, column=0, columnspan=2)
 
win.mainloop()