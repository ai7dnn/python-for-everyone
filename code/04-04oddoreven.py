#%% 04-04oddoreven.py	정수의 홀수와 짝수 판정
n = int(input('정수 입력 >> '))
#n = 10
if n%2 == 0: #2로 나느어 떨어지는지 검사, 결국 True이면 짝수 False이면 홀수
    print('%d은 짝수이다.' % n)
else: 
    print('%d은 홀수이다.' % n)
