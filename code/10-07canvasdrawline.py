#%% 10-07canvasdrawline.py	캔버스에 직선 그리기 
from tkinter import *

win = Tk()
win.title('라인 그리기')
win.geometry('640x400+100+100')

def click(event):
    global sX, sY
    print("클릭 위치", event.x, event.y)
    sX, sY = event.x, event.y

def release(event):
    global eX, eY
    print("릴리즈 위치", event.x, event.y)
    eX, eY = event.x, event.y
    #직선 라인 그리기
    canvas.create_line(sX, sY, eX, eY, fill="blue", width=2)   

canvas = Canvas(win, relief='solid', bd=2)
canvas.pack(expand=True, fill='both')

#왼쪽 마우스 버튼 클릭 바인딩
canvas.bind("<Button-1>", click) 
#왼쪽 마우스 버튼 릴리즈 바인딩
canvas.bind("<ButtonRelease-1>", release) 

win.mainloop()