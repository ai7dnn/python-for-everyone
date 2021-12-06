a = int(input('정수 하나를 입력하세요 >> '))
#a = 23
mask = 0b1111 #0xf도 가능
print('정수 {0} 2진수로는 {0:b}'.format(a))
print('가장 오른쪽 4비트: {0:04b} 정수로는 {0}'.format(a & mask))
