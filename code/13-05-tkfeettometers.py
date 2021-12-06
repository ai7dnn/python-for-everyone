#%% Mini Project 5 13-05-tkfeettometers.py
from tkinter import *

#피트를 미터로 변환하여 미터 레이블에 반영, 예외 처리 구현
def calculate(*args):
    try:
        value = float(feet.get())
        meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError as e:
        print('피트(feet) 입력에 문제가 있습니다.')
        print('예외발생 이름: {}'.format(type(e)))
        print('예외발생 이유: {}'.format(e))
        feet.set('다시 입력하세요!')
    else:
        print('피트(feet) 입력이 잘 되었습니다.')
        print('피트(feet) 입력 값:', value) #디버깅을 위해 출력
    finally:
        print('피트(feet) 입력 예외 처리가 잘 되는군요!')
    
root = Tk()
root.title("피트에서 미터로 변환")

#다른 위젯을 구성할 수 있는 프레임 위젯을 생성해 윈도 바탕에 추가
mainframe = Frame(root, padx=10, pady=5)
mainframe.grid(column=0, row=0)

#피트와 미터 위젯에 표시되는 문자열 수정을 위한 문자열변수를 생성해 설정 
feet = StringVar()
meters = StringVar()
#위 문자열변수를 각 위젯과 연결 
entfeet = Entry(mainframe, textvariable=feet, width=14, )
lbmeter = Label(mainframe, textvariable=meters, relief='ridge')
entfeet.grid(column=0, row=0, sticky=(W, E))
lbmeter.grid(column=0, row=1, sticky=(W, E))

Label(mainframe, text="피트(feet)").grid(column=1, row=0, sticky=W)
Label(mainframe, text="미터(meters)").grid(column=1, row=1, sticky=W)

#버튼을 누루면 함수 calculate가 호출되도록 연결 
bntcalc = Button(mainframe, text="Calculate", width=36, command=calculate)
bntcalc.grid(column=0, row=2, columnspan=2, sticky=W)

#프레임에 포함되어 있는 하위 위젯들을 반환하여 가로 세로 공간을 일괄적으로 수정 
for child in mainframe.winfo_children(): 
	child.grid_configure(padx=5, pady=3)

#바로 피트를 입력할 수 있도록 촛점을 지정 
entfeet.focus()
#리턴 키에도 변환 계산이 되도록 키와 변환 함수를 연결  
root.bind('<Return>', calculate)

root.mainloop()
