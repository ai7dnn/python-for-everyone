value = input('실수(3자리.2자리로 345.78처럼)를 하나 입력하세요. >> ')
#value = '345.34'
num = value.replace('.', '')

sum = 0
sum += int(num[0])
sum += int(num[1])
sum += int(num[2])
sum += int(num[3])
sum += int(num[4])
print('입력 값:', value)
print('모든 자릿수 합:', sum)
