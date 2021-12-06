#인자 name의 기본 값을 '여러분'으로 지정
def hello(name = '여러분'):
    print('안녕, {}!'.format(name))
    
hello() #name으로 기본 값 사용
hello('현철') #name으로 지정된 '현철' 사용
