#함수 정의
def hello(name):
    #전달받은 인자 name을 함수 정의에서 사용
    print('안녕, {}!'.format(name)) #인자 name에게 인사

hello('수빈') #함수 호출, 수빈에게 인사
sname = '현수' 
hello(sname) #함수 호출, 현수이게 인사
