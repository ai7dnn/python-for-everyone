def mysum(x, y = 0): #인자가 두 개 
    """두 수의 합 반환 함수"""
    return x + y # 두 인자의 합으로 반환

hap = mysum(5) #y는 기본 값이 0으로     
print(hap)

hap = mysum(5, 10)    
print(hap)
