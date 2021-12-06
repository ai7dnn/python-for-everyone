#%% 05-07nestedanimallist.py	동물의 분류를 리스트로 처리 
animal = [['사자', '코끼리', '호랑이'], '조류', '어류']
print(animal)

for s in animal:
    print(s)
print()

bird = ['독수리', '참새', '까치']
fish = ['갈치', '붕어', '고등어']
animal[1:] = [bird, fish] 
print(animal)

for lst in animal:
    for item in lst:
        print(item, end = ' ')
    print() 
print()