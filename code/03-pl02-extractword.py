#단어를 추출하여 회문(palindrome)인지 검사 
str = input('콤마로 구분된 단어 3개 입력 >> ')
#str = '기러기,  level, 아버지'
str = str.replace(' ', '')
w1, w2, w3 = str.split(',')

print('단어: {}, 역순: {}, 회문: {}'.format(w1, w1[::-1], (w1 == w1[::-1])))
print('단어: {}, 역순: {}, 회문: {}'.format(w2, w2[::-1], (w2 == w2[::-1])))
print('단어: {}, 역순: {}, 회문: {}'.format(w3, w3[::-1], (w3 == w3[::-1])))