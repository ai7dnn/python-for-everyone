#진수와 그에 맞는 정수를 입력 받아 2진수, 8진수, 10진수, 16진수 출력	
base = int(input('입력할 정수의 진수(base)는? '))
invar = input(str(base) + '진수 정수 입력 >> ')
data = int(invar, base) #입력 문자열을 base 진수로 변환
#여러 진수로 출력
print('2진수:', bin(data))
print('8진수:', oct(data))
print('10진수:', data)
print('16진수:', hex(data))
