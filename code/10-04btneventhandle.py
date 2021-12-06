#%% 10-04btneventhandle.py	버튼으로 레이블의 정수 값 증가와 감소 
from tkinter import *

def add(): #1 증가시켜 레이블의 문자열에 지정
    n = int(count.get())
    n += 1
    count.set(n)

def sub(): #1 감소시켜 레이블의 문자열에 지정
    n = int(count.get())
    n -= 1
    count.set(n)

str = ['더하기', '빼기']

win = Tk()

#레이블에 표시되며, 값이 값이 쉽게 레이블에 반영될 값인 count
#tkinter가 제공하는 StringVar라는 객체에 저장
count = StringVar(value = '0') #count.set('0') 또는 value 인자에 첫 값인 0을 지정
#이후 count.get()으로 참조하고 count.set(값)으로 지정 

#키워드 인자 textvariable: 레이블에 표시할 값을 가져올 변수
#키워드 인자 textvariable에 위에서 만든 StringVar 변수인 count를 설정
data = Label(win, width = 20, textvariable = count)
data.grid(row=0, column=0, columnspan=2)

badd = Button(win, text=str[0], command = add) #누르면 함수 add() 호출
badd.grid(row=1, column=0)
bsub = Button(win, text=str[1], command = sub) #누르면 함수 sub() 호출
bsub.grid(row=1, column=1)

win.mainloop()