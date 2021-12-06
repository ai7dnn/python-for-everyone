#%% 09-03myrandom.py	모듈 random을 활용한 난수 발생 함수 구현
import random

def nrandom(start, end, n, duplicated = False):
    ''' 
    start와 end 사이의 정수 난수를 n개 생성하여 반환
    인자
        start: 시작 정수
        end: 마지막 정수
        n: 난수 개수
        duplicated: 중복허용 여부, 기본은 중복하지 않음         
    '''
    lst = [] #반환할 난수 리스트
    if duplicated:
        for _ in range(n):
            lst.append(random.randint(start, end))
    else:
        lst = list(random.sample(range(start, end+1), n))
    #모두 정렬하여 반환
    return sorted(lst)     

if __name__ == '__main__':  
    print('로또 복권: ', nrandom(1, 45, 6))
    print('주사위 3번: ', nrandom(1, 6, 3, True))
