#%% 11-07readlinefile.py	파일에서 한 줄씩 읽어 콘솔에 출력 처리 
f = open('pyzen.txt', 'r')

while True:
    line = f.readline()
    if not line: break
    print(line, end = '')
    #print(line.strip('\n'))
f.close()
