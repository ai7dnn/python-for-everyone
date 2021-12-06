def ctofahrenhite(cels):
    """ 인자인 섭씨온도 cels을 화씨 온도로 변환하여 반환 """
    return cels * 9/5 + 32

def ftocelsius(fahr): 
    """ 인자인 화씨온도 fahr을 섭씨 온도로 변환하여 반환 """
    return (fahr - 32) * 5/9
    
for cels in range(28, 35, 2):
    print('섭씨: {}, 화씨: {:.2f}'.format(cels, ctofahrenhite(cels)))
    
for fahr in range(90, 103, 3):
    print('섭씨: {:.2f}, 화씨: {}'.format(ftocelsius(fahr), fahr))
