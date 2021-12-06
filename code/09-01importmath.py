#%% 코딩 09-01importmath.py 
import math 
print(math.pi) #원주율 pi

from math import e #자연수 e
print(math.e)
from math import degrees, radians
print(degrees(math.pi), radians(90))
from math import floor, ceil #바닥 값, 천정 값 함수
print(floor(3.8), ceil(3.1))
from math import factorial as fact #n! 함수
print(fact(5))