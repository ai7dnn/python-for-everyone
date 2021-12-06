#%% 04-11burgerorder.py 번호로 버거 메뉴 주문 받기 
menu = '''버거, 콤보 번호로 주문하세요!
    0. 주문종료 
    1. 올인원팩
    2. 투게더팩
    3. 트리오팩
    4. 패밀리팩
        >> ''' 
        
more = True
while more:
    order = int(input(menu))
    if order == 1:
        print('%s 주문' % '올인원팩')
    elif order == 2:
        print('%s 주문' % '투게더팩')
    elif order == 3:
        print('%s 주문' % '트리오팩')
    elif order == 4:
        print('%s 주문' % '패밀리팩')
    elif order == 0:
        print('주문종료'.center(20, '*'))
        more = False
    else:
        print('모르겠어요.')
else:
    print('주문을 마치겠습니다.')
