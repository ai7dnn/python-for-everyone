#%% 05-10wordsort.py	한 글자 단어와 과일의 정렬
word = list('삶꿈정')
word.extend('복빛')
print(word)
word.sort()
print(word)
 
fruit = ['복숭아', '자두', '골드키위', '귤']
print(fruit)
fruit.sort(reverse=True)
print(fruit)

mix = word + fruit
print(sorted(mix))
print(sorted(mix, reverse=True))