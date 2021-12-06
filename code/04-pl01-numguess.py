#%% 프로젝트 Lab1 04-pl01-numguess.py 1에서 10 사이의 수 맞추기 
import random
answer = random.randint(1, 10)

indata = int(input('1에서 10사이의 수를 맞추세요 >> '))
while True:
    if indata == answer:
        print('축하합니다. {}: 정답입니다.'.format(indata))
        break;
    elif indata < answer:   
        str = '{}보다 더 큰 수로 다시 입력 >> '.format(indata)
    else:
        str = '{}보다 더 작은 수로 다시 입력 >> '.format(indata)
    indata = int(input(str))

print(" 종료 ".center(30, '*'))
