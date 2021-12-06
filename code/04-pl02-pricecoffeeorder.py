#%% 프로젝트 Lab2 04-pl02-pricecoffeeorder.py 커피 주문받아 주문 가격 표시 난이도: 실전
menu = '''Coffee menu!
    1. 아메리카노    2000
    2. 카페라떼      2500
    3. 카푸치노      3000
    4. 카라멜마키아또 4000
    0. 주문종료 
종류 ? ''' 
            
print('환영합니다. 마실 것 선택하세요')
total = 0
while True:
    order = int(input(menu))
    if order == 0:
        print()
        print('주문종료 '.center(18, '*'))
        break
    else: 
        cnt = int(input('수량 ? '))
        if order == 1:
            total += cnt * 2000 
            print('\n%s %d개 주문' % ('아메리카노', cnt))
        elif order == 2:
            total += cnt * 2500 
            print('\n%s %d개 주문' % ('카페라테', cnt))
        elif order == 3:
            total += cnt * 3000 
            print('\n%s %d개 주문' % ('카푸치노', cnt))
        elif order == 4:
            total += cnt * 4000 
            print('\n%s %d개 주문' % ('카라멜마키아또', cnt))
        else:
            print('모르겠어요.')
        print('현재 주문 가격: %d원' % total)
        print()
        
print('총 주문 가격: %d원' % total)
print(' 안녕! '.center(20, '='))
