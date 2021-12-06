invar = input('16진수 정수 입력 >> ')
data = int(invar, 16) #입력 문자열을 16진수로 인지하여 변환
#여러 진수로 출력
print('2진수:', bin(data))
print('8진수:', oct(data))
print('10진수:', data)
print('16진수:', hex(data))
