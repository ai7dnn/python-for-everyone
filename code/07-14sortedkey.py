#%% 7-14. 코딩	07-14sortedkey.py	내장 함수 sorted()에서 키워드 인자 key 활용	난이도: 응용
words = "The core of extensible programming is defining functions.".split()
#각 항목 단어를 모두 소문자로 바꾼 항목을 키로 정렬 
print(sorted(words, key = str.lower))
#각 항목 단어의 첨자 1, 두 번째 문자를 키로 정렬 
print(sorted(words, key = lambda word: word[1])) 

groupnumber = [('잔나비', 5), ('트와이스', 9), ('블랙핑크', 4), ('방탄소년단', 7)]
# 항목의 첫 번째 항목을 키로 정렬 
print(sorted(groupnumber))
# 항목의 두 번째 항목인 그룹 인원수를 키로 정렬 
print(sorted(groupnumber, key = lambda singer: singer[1]))
