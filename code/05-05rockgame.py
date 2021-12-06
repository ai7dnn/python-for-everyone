#%% 05-05rockgame.py	가위 바위 보 리스트 항목 참조
rsp = ['가위', '바위', '보']
for i in range(len(rsp)):
    print(rsp[i], end=' ')
print()

from random import choice
print('컴퓨터의 가위바위보 5개')
for i in range(5):
    print(choice(rsp))
