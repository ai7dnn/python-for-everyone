#%% 프로젝트 Lab 11-pl02-createtextfile.py	텍스트 파일을 생성하여 콘솔에 출력
while True:
    try:
        fname = input('파일명 입력 >> ')
        if fname == '':
            raise Exception('파일 이름을 입력하세요.')
    except Exception as e:
        print('예외 발생 이유: %s' % e)
    else:
        print('입력한 파일 이름: ', fname)
        break
    finally:
        print('예외 처리 수행')
    
with open(fname, 'w') as f:
    print('\n파일 %s에 여러 줄을 저장할 예정입니다.' % fname)
    print('한 줄씩 입력한 후 엔터를 누르시고')
    print('더 이상 없으시면 줄의 첫 열에서 그대로 엔터를 치세요!')
    
    while True:
        line = input()
        if not line: break
        f.write(line + '\n')
print(' 파일 쓰기 완료! '.center(30, '*'))

with open(fname, mode='rt') as f:
    for line in f:
        print(line, end='')
print(' 파일 읽기 완료! '.center(30, '*'))
