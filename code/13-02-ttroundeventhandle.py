import random as r
import turtle as t            

cols = ['red', 'blue', 'green', 'purple', 'magenta',
        'gray', 'yellow', 'cyan', 'orange', 'aqua']

width, height = 500, 500

#윈도를 벗어나는지 검사하여 반대로 나오도록    
def checkround():
    #내부 함수로 반대로 이동하며 터틀의 색상을 임의로 수정 
    def round(x, y):
        t.ht(); t.pu()
        t.goto(x, y)
        t.pd(); t.st()
        t.pencolor(cols[r.randint(0, len(cols)-1)])

    x, y = t.pos()
    #print(x, y)

    #x 좌표를 벗어나면 그 반대로 이동
    if not (-width/2 < x < width/2):
        round(-x, y)
        
    #y 좌표를 벗어나면 그 반대로 이동
    if not (-height/2 < y < height/2):
        round(x, -y)    
       
               
def goright():
    t.setheading(0)
    t.fd(10)
    checkround()

def goleft():
    t.setheading(180)
    t.fd(10)
    checkround()

def goup():
    t.setheading(90)
    t.fd(10)
    checkround()

def godown():
    t.setheading(270)
    t.fd(10)
    checkround()

def cls():
    t.clear()

t.setup(width, height) #초기 원도의 크기 조정
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
