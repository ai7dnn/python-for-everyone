str = input('두 개의 단어를 빈 공간으로 구분하여 입력하세요. >> ')
pos = str.find(' ')
preWord = str[:pos]
postWord = str[pos+1:]
print(preWord, postWord) 
print(preWord[::-1], postWord[::-1]) 
