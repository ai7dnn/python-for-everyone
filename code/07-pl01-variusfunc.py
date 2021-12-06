#%% 프로젝트 Lab 1	07-pl01-variusfunc.py	1에서 100까지 10개의 정수로 간단한 함수 이용
from random import randint

def setsequence(start, end, count):
    ''' 전역변수 nums에 start(1)~end(100) 사이의 정수 count(10)개 추가 '''
    global nums
    for _ in range(count):
        nums.append(randint(start, end))
        
nums = []
setsequence(1, 100, 10)
print(sorted(nums))
print('합: %d,  평균: %.2f' % (sum(nums), sum(nums)/len(nums)))
print('최대: %d,  최소: %d' % (min(nums), max(nums)))
