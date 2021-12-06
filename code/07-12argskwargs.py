#%% 07-12argskwargs.py	가변 인자와 키워드 형태 가변 인자 함수 구현
def sumvalue(*values, **kwargs):
    hap = 0
    #가변 인자 합 구하기
    for v in values:
        hap += v
    #키워드 인자 합 구하기
    for key in kwargs:
        hap += kwargs[key]
    return hap
    
coffeeprice = {'value': 2000,'에스프레소': 2000, '아메리카노': 2800, '카페라떼': 3200}
print(sumvalue(1, 2, 3, **coffeeprice)) 
print(sumvalue(*[2, 3, 4], **coffeeprice)) 
#print(sumvalue(**coffeeprice, *[2, 3, 4])) #오류 발생
