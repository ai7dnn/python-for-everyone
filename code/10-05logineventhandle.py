#%% 10-05logineventhandle.py	로그인 과정의 이벤트 처리 
from tkinter import *

users = dict(python='power', java='beauty')

def checkid():
    uid = et1.get().strip() #입력된 사용자 이름 문자열 받기
    pwd = et2.get().strip() #입력된 암호 문자열 받기
    print(uid, pwd)
    if uid in users.keys(): #사용자 이름이 있는지 검사
        if users[uid] == pwd: #사용자 이름과 암호 일치
            print('로그인 성공')
        else:
            print('암호를 확인하세요.')
    else:
        print('사용자 이름을 확인하세요.')

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
bt1 = Button(lb, text='OK', command = checkid) # 버튼을 누르면 checked 함수 호출
bt2 = Button(lb, text='CANCEL')
bt1.grid(row=0, column=0, padx = 10) # 외부 여백을 10을 둠
bt2.grid(row=0, column=1, padx = 10) # 외부 여백을 10을 둠
 
win.mainloop()
