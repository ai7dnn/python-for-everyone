#%% 11-01basictryexcept.py	잘못된 문자열을 정수로 변환 시 예외 처리 
try:
    data = int('3.67')
except Exception as e:
    print('예외발생 이름: {}'.format(type(e)))
    print('예외발생 이유: {}'.format(e))
