season = {'봄': 'spring', '여름': 'summer', '가을': 'autumn', '겨울': 'winter'}
print(season.keys())
print(season.items())
print(season.values())

#메소드 keys()로 항목 순회
for key in season.keys():
    print('%s %s  ' % (key, season[key]))

for item in season.items():
    print('{} {}  '.format(item[0], item[1]), end= ' ')
print()
#메소드 items()의 반환 값인 튜플을 한 변수에 저장한 경우, 항목 순회 2
for item in season.items():
    print('{} {}  '.format(*item), end= ' ')
print()
