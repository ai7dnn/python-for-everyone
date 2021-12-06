#%% 04-09findnum.py	지정된 최소 한 자릿수가 포함된 두 자리 정수 찾기  
n = input("10진수의 한 자릿수 입력 >> ")
print('두 자릿수 정수에서 최소 한 자리수가 %s인 정수 찾기: ' % n)
print(' 결과 '.center(50, '='))

for i in range(10, 100):
    snum = str(i)
    if n in snum:
        print(i, end= ' ')
