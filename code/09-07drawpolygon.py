#%% 09-07drawpolygon.py	함수 정의로 다각형 그리기
import turtle as t

#색상 리스트
cols = ['red', 'blue', 'green', 'purple', 'magenta', 'black',
        'gray', 'yellow', 'cyan', 'orange', 'aqua']

def drawpolygon(n, size):
    ''' 한 변의 길이가 size인 n각형 그리기 '''
    for i in range(n):
        t.pencolor(cols[i % len(cols)]) #펜 색상 지정 
        t.forward(size) #선 그리기
        t.left(360/n) #각도 수정

t.setup(500, 400) #초기 원도의 크기 조정
t.speed(3) #1에서 10까지 거북이 속도 증가, 0이면 최고속

t.pu() #이동에 선이 그려지지 않도록  
t.goto(-50, -170) #처음 위치로 이동
    
t.pd() #다갹형을 그리기 위해 꼬리를 내리고 
#한 변의 길이가 100인 다각형 그리기 
for i in range(3, 12):
    drawpolygon(i, 100) #함수 호출 