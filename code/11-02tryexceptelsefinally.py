#%% 11-02tryexceptelsefinally.py	IndexError 예외 처리
lst = ['C/C++', 'java', 'c#', 'python']

try:
    print(lst[4])
#    print(lst[0])
except Exception as e:
    print('예외발생 이름: {}'.format(type(e)))
    print('예외발생 이유: {}'.format(e))
else:
    print('예외 없이 잘 실행되었습니다.')
finally:
    print('예외처리가 잘 되는군요!')