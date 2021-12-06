#%% Mini Project 1 13-01-tteventhandle.py
import turtle as t            

#이벤트에 처리할 함수를 정의    
def goright():
    t.setheading(0)
    t.fd(10)

def goleft():
    t.setheading(180)
    t.fd(10)

def goup():
    t.setheading(90)
    t.fd(10)

def godown():
    t.setheading(270)
    t.fd(10)

def cls():
    t.clear()

t.setup(500, 500) #초기 원도의 크기 조정
t.shape('turtle')    
t.clear()
t.home()

#함수와 키보드 키를 연결하여 이벤트가 작동하도록
t.onkeypress(goright, 'Right')
t.onkeypress(goleft, 'Left')
t.onkeypress(goup, 'Up')
t.onkeypress(godown, 'Down')
t.onkeypress(cls, 'Escape')
t.listen()

