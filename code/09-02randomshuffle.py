#%% 코딩 09-02randomshuffle.py 모듈 random의 주요 함수
import random as rd

for i in range(3):
    print(rd.random()) #0에서 1보다 작은 실수 난수 생성

cards = [[1, '송학'], [2, '메조'], [3, '벚꽃'], [4, '흑싸리'], [5, '초'], [6, '모란']]   
print(cards)
for _ in range(3):
    rd.shuffle(cards) #카드를 섞음
    print(cards)

print(rd.sample(cards, 2)) #카드에서 2개를 선택
