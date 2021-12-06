def hello(): #함수 정의
    print('\tHello, Python!')

def helloint(): #함수 정의
    print('\t', 77)

print('처음 하는 함수 호출 hello()')
hello() #함수 호출
print('함수 호출 hello() 이후')

print(1)
print(helloint) #메모리에 저장된 함수 확인
helloint() #함수 호출
print(3)
