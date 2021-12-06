#%% 11-09forinfile.py	파일 자체를 사용해 한 줄씩 읽어 콘솔에 출력 처리 
lst = ['파일 처리 모드\n', "mode='x'\n", "mode='rt'\n" ]

try:
    with open('modex.txt', mode='x') as file:
        file.writelines(lst)
    print(' 파일 쓰기 완료! '.center(30, '*'))
    
except FileExistsError as e:
    print(e)
    print(' 파일 쓰기 실패! '.center(30, '*'))
    
else:
    with open('modex.txt', mode='rt') as file:
        for line in file:
            print(line, end='')
    print(' 파일 읽기 완료! '.center(30, '*'))