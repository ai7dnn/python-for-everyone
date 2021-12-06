#%% 09-04importkutil.py	직접 만든 모듈 kutil의 함수 nrandom 불러 활용
from kutil import nrandom

for i in range(5):
    print('로또 복권 %d:' % (i+1), nrandom(1, 45, 6))
print()    
print('주사위 4번: ', nrandom(1, 6, 4, True))
