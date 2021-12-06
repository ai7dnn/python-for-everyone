#%% 04-16dayspelltest.py	월 화 수 중의 영어 철자 하나 검사
days = ['monday', 'tuesday', 'wednesday']

while True:
    user = input('월 화 수 중의 하나 영어 단어 입력 >> ')
    if user not in days:
        print('잘못 입력했어요!')
        continue
    print('입력: %s, 철자가 맞습니다.' % user)
    break

print(' 종료 '.center(15, '*'))
