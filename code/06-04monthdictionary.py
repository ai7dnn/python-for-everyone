month = {1: 'January', 2: 'February', 3: 'March', 4: 'April'}
month[5] = 'May'
month[6] = 'June'
month[7] = 'July'
month[8] = 'August'
month[9] = 'September'
print(month)
print()

from random import randint
#임의로 5번의 월 단어 출력
for i in range(5):
    r = randint(1, 9)
    print('%d: %s' % (r, month[r]))
