#%% 프로젝트 Lab 09-pl02-drawmodhexagon.py	터틀로 변형된 육각형 그리기
import turtle as t            

#선 색상에 사용할 이름 리스트 
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t.setup(500, 400) #초기 원도의 크기 조정
t.bgcolor('black') #바탕색 변경

for i in range(180):
    t.pencolor(colors[i % len(colors)])
    t.width(i/100 + 1)
    t.forward(i)
    t.left(59)