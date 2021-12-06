#%% 04-10checkrides.py 어린이를 위한 놀이기구 탑승 검사
MAXNUM = 4
MAXHEIGHT = 130

more = True
cnt = 0
while more:
    height = float(input("키는 ? "))
    if height < MAXHEIGHT:
        cnt += 1
        print('들어가세요.', '%d명' % cnt)
    else: 
        print('커서 못 들어갑니다.')
    if cnt == MAXNUM:
        more = False
else: 
    print('%d명 모두 찼습니다. 다음 번에 이용하세요.' % cnt)
