#%% 프로젝트 Lab 11-pl01-raiseexception.py 표준 입력 값의 다양한 예외 처리
while True:
    try:
        base = int(input('입력할 정수의 진수(base)는? [2, 8, 10, 16 중의 하나] '))
        if not base in (2, 8, 10, 16):
            raise ValueError('2, 8, 10, 16 중의 하나를 입력하세요')
    except Exception as e:
        print('예외발생 원인: %s\n' % e)
    else:
        print()
        break

check = {2:'01', 8:'01234567', 10:'0123456789', 16:'0123456789abcdefABCDEF'}
while True:
    try:
        invar = input(str(base) + '진수 정수 입력 >> ')
        for digit in invar:
            if digit not in check[base]:
                raise ValueError('%d진수를 입력하세요' % base)
    except Exception as e:
        print('예외발생 원인: %s\n' % e)
    else:
        print()
        break

data = int(invar, base) #입력 문자열을 base 진수로 변환
#여러 진수로 출력
print('2진수:', bin(data))
print('8진수:', oct(data))
print('10진수:', data)
print('16진수:', hex(data))
