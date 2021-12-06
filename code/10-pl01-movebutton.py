#%% 프로젝트 Lab 10-pl01-movebutton.py	마우스를 도망가는 버튼 
from random import randrange
from tkinter import *

#버튼에 마우스가 들어오면 버튼 위치를 이동시키는 함수
def escapemouse(e):
    #윈도 전체 크기 저장
    w = win.winfo_width()
    h = win.winfo_height()
    print('원도 크기: ', w, h)
    #버튼 크기 저장
    bw = btn.winfo_width()
    bh = btn.winfo_height()
    print('버튼 크기: ', bw, bh)
    #난수로 그려질 버튼이 보이도록 위치 (rx, ry) 지정
    rx = randrange(0, w - bw)
    ry = randrange(0, h - bh)
    #위치로 버튼 이동 
    print('이동 위치: ', rx, ry)
    btn.place(x=rx, y=ry)

win = Tk()
win.geometry("600x300+100+100")
win.title('마우스를 도망가는 버튼')
win.resizable(False, False)

btn = Button(win, text='저를 눌러 보세요!', command=win.quit)
#버튼의 첫 위치 지정
btn.place(x=200, y=30)
#btn.place(relx=0.5, rely=0.5)

#마우스가 버튼 위로 들어오면 함수 escapemouse가 실행되도록 연결
btn.bind('<Enter>', escapemouse)

win.mainloop()
