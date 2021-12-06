#%% 11-06writereadfile.py 파일에 ‘파이썬 철학’ 쓰기와 읽기 
f = open('pyzen.txt', 'wt')
f.write('파이썬 철학\n')
f.write('아름다움이 추한 것보다 낫다.\n')
f.write('명시적인 것이 암묵적인 것보다 낫다.\n')
f.close()

f = open('pyzen.txt', mode='r')
s = f.read() 
print(s)
f.close()