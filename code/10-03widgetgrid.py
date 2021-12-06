#%% 10-03widgetgrid.py	테이블 형태 배치 그리드(grid) 
from tkinter import *
win = Tk()
win.title('사용자 인증')

lb1 = Label(win, text='사용자 이름')
lb2 = Label(win, text='암호')
lb1.grid(row = 0, column = 0, sticky = E) #현 구역에서 위치를 오른쪽 조정
lb2.grid(row = 1, column = 0, sticky = E) #현 구역에서 위치를 오른쪽 조정

et1 = Entry(win)
et2 = Entry(win)
et1.grid(row = 0, column = 1)
et2.grid(row = 1, column = 1)

#가장 하단에 버튼 2개를 저장할 레이블을 생성해 배치
lb = Label(win)
lb.grid(row=2, column=0, columnspan=2) # 두 열을 합해서 배치
bt1 = Button(lb, text='OK')
bt2 = Button(lb, text='CANCEL')
bt1.grid(row=0, column=0, padx = 10) # 외부 여백을 10을 둠
bt2.grid(row=0, column=1, padx = 10) # 외부 여백을 10을 둠
 
win.mainloop()