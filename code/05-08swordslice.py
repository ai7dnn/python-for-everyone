#%% 05-08swordslice.py  한 글자의 한국 단어로 이해하는 리스트 슬라이싱 
wlist = ['밥','삶','길','죽','꿈','차','떡','복','말']
print('wlist[:] = ', wlist[:])
print('wlist[::] = ', wlist[::])
print('wlist[::-1] = ', wlist[::-1])
#오름차순
print(wlist[::3])
print(wlist[1::3])
print(wlist[2::3])
#내림차순
print(wlist[::-2])
print(wlist[-1:-8:-3])
#오름과 내림차순의 혼재
print(wlist[1:-1:])
print(wlist[-2:-9:-3])

#wlist = list('밥삶길죽꿈차떡복말')
