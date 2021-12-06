#%% 10-02widgetpack.py	다양한 위젯 구성 
from tkinter import *

win = Tk()
win.title('여러 위젯 구성')
 
lbl = Label(win, text="레이블(Label)") #레이블
lbl.pack() #레이블을 윈도에 맞게 적정하게 배치
 
txt = Entry(win) #엔트리
txt.insert(0, '엔트리(Entry)')
txt.pack()
 
btn = Button(win, text="OK") #버튼
btn.pack()
 
win.mainloop()