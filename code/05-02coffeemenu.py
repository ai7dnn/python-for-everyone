#%% 05-02coffeemenu.py 간단한 커피 메뉴 만들기 1
menu = ['COFFEE', 'BEVERAGE', 'ADE']
coffee = ['에스프레소', '아메리카노', '카페라떼', '카페모카']

print('='*45)
for category in menu:
    print('{:^15s}'.format(category), end=' ')
print()
print('='*45)

for ckind in coffee:
    print('{:^10s}'.format(ckind))    
