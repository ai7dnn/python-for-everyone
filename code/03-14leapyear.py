year = int(input('윤년을 검사할 년도 입력 >> '))
#year = 2020
print('입력한 년도: %d' % year)
cond1 = year % 4 == 0
cond2 = year % 100 != 0
cond3 = year % 400 == 0
result1 = cond1 and cond2 or cond3
print('개별 검사 {} and {} or {}: {}'.format(cond1, cond2, cond3, result1))
result2 = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
print('통합 검사: %s' % result2)