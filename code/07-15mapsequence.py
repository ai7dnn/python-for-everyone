#%% 07-15mapsequence.py	내장 함수 map()을 활용한 원 면적 구하기
circle = [3, 5, 7, 10]
area = list(map(lambda r: r * r * 3.14, circle)) 

for c, a in zip(circle, area):
    print('반지름 {} => 원면적 {}'.format(c, a))
