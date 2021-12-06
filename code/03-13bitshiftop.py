num = int(input('이동 연산 num << cnt를 수행할 정수 num 입력 ? '))
cnt = int(input('이동 연산 num << cnt를 수행할 정수 cnt 입력 ? '))
#num = 0b00010111
#cnt = 3
print('{0:032b} {0:8d} :num'.format(num))
print('{2:032b} {2:8d} :{0} << {1}'.format(num, cnt, num << cnt))
print('{2:032b} {2:8d} :{0} * 2**{1}'.format(num, cnt, num * 2**cnt))
