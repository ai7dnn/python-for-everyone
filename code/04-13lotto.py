#%% 04-13lotto.py	1에서 45까지의 6개 수를 맞히는 로또 
winnumber = 11, 17, 28, 30, 33, 35
print(' 모의로또 당첨번호 '.center(28, '='))
print(winnumber)
print()
print(' 내 번호 확인 '.center(30, '-'))
cnt = 0
import random
for i in range(6):
    n = random.randint(1, 45)
    if n in winnumber:
        print(n, 'O ', end = ' ')
        cnt += 1
    else: 
        print(n, 'X ', end = ' ')

print()
print(cnt, '개 맞음')
