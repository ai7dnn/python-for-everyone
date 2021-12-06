#구기 종목 리스트
sports = ['축구', '야구', '농구', '배구']
#위 종목에 대응하는 팀원 수를 항목으로 구성 
num = [11, 9, 5, 6]
print(sports)
print(num)
print()

print('함수 zip():')
for s, i in zip(sports, num):
    print('%s: %d명' % (s, i), end = ' ')    
print()
for tp in zip(sports, num):
    print('{}: {}명'.format(*tp), end = ' ')    
print(); print()

#dict()와 zip() 함수로 종목이름을 키로 인원수를 값으로 저장
print('함수 dict(zip()):')
sportsnum = dict(zip(sports, num))
print(sportsnum)
