#%% 10-08imagecanvas.py	이미지 파일을 캔버스에 그리기
from tkinter import *

win = Tk()
win.title("그림 로드")
win.geometry("660x930")

#캔버스 생성
canvas = Canvas(win, bg='Yellow')
#캔버스를 윈도에 배치, 가로 세로로 확장되게
canvas.pack(expand=YES, fill=BOTH)

#사진 생성
img = PhotoImage(file="imitation.png")
#사진을 캔버스 위에 생성
canvas.create_image(10, 10, anchor=NW, image=img)

win.mainloop()