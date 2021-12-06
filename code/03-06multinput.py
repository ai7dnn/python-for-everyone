m, n, x, y = input('4개의 수 입력 >> ').split()
a, b, c, d = float(m), float(n), float(x), float(y)
print('입력 값: ', a, b, c, d)
sum = a + b + c + d
print('합: ', sum, '평균: ', sum / 4)
print('최대: ', max(a, b, c, d), '최소: ', min(a, b, c, d))