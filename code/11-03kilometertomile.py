#%% 11-03kilometertomile.py  마일로 변환 시 예외 처리
from tkinter import *

def tomile(kilometer):
    return round(kilometer * 0.6213, 2)

def clicked():
    def insertmile(sdata):
        mile.delete(0, END) #이전의 자료를 비우고
        mile.insert(0, sdata) #새로 변환된 자료를 쓰고
    try:
        fmeter = float(kmeter.get()) #엔트리 kmeter에서 값 가져오기
    except ValueError as e:
        print('킬로미터 입력에 문제가 있습니다.')
        print('예외발생 이름: {}'.format(type(e)))
        print('예외발생 이유: {}'.format(e))
        insertmile('다시 입력하세요!')
    else:
        print('킬로미터 입력이 잘 되었습니다.')
        print('킬로미터 입력 값:', fmeter) #디버깅을 위해 출력
        insertmile(str(tomile(fmeter)))
    finally:
        print('킬로미터 입력 예외처리가 잘 되는군요!')

win = Tk()
win.title('거리 킬로미터(km)를 마일(mile)로 변환')
 
lbcel = Label(win, text="킬로미터(km)", width=20)
lbfar = Label(win, text="마일(mile)")
lbcel.grid(row=0, column=0)
lbfar.grid(row=1, column=0)

kmeter = Entry(win, width=20)
mile = Entry(win)
kmeter.grid(row=0, column=1)
mile.grid(row=1, column=1)

cvt = Button(win, text="마일(mile)로 변환", width=20, command = clicked)
cvt.grid(row=2, column=0, columnspan=2)
 
win.mainloop()
