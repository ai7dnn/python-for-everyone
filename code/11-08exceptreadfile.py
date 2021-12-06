#%% 11-08exceptreadfile.py	파일 읽기에 예외 처리 
try:
    f = open('pyzen.txt', mode='r')
    
except FileNotFoundError as e:
    print(e)
    print(' 파일 읽기 실패! '.center(30, '*'))
else:     
    for line in f.readlines():
        print(line.strip('\n'))
    f.close()
    print(' 파일 읽기 완료! '.center(30, '*'))
finally:
    print(' 프로그램 종료! '.center(30, '*'))