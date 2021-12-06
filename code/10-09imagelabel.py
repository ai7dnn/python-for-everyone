#%%	10-09imagelabel.py	이미지 파일을 레이블에 그리기	난이도: 기본
from tkinter import *

win = Tk()
win.title("레이블 그림 로드")

#사진 생성
img = PhotoImage(file="imitation.png")
#사진을 담은 레이블 생성
lbimg = Label(win, image=img)
#캔버스를 윈도에 배치, 가로 세로로 확장되게
lbimg.pack()

win.mainloop()
