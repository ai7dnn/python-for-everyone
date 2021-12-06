#%% 11-04variustryexcept.py	두 정수의 곱과 나눔 연산에서의 예외 처리 구현 
while True:
    try:
        xstr = input('정수 입력 > ')
        x = int(xstr)
        y = int(input('0이 아닌 정수 입력 > '))
        prod = x * y
        divd = x / y
        
    except ZeroDivisionError as exp:
        print('except ZeroDivisionError as exp:')
        print('\t예외발생 이름: {}'.format(type(exp)))
        print('\t예외발생 이유: {}'.format(exp))
        print('\t0으로는 나눌 수 없습니다.')
    except ValueError as exp:
        print('except ValueError as exp:')
        print('\t예외발생 이름: {}'.format(type(exp)))
        print('\t예외발생 이유: {}'.format(exp))
        print('\t입력한 값이 정수가 아닙니다.')    
        
    else:
        print('{} × {} = {}'.format(x, y, prod))
        print('{} ÷ {} = {}'.format(x, y, divd))
        
    finally:
        if xstr in ['x', 'X']:
            print('종료 합니다.')
            break
        print('다시 해 보세요.\n')
