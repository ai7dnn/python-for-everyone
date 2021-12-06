#%% 09-09matrixop.py	2차원 행렬의 사칙 연산과 함수 matmult()
import numpy as np
data1 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
data2 = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]
mA = np.array(data1)
mB = np.array(data2)
print('각각의 2차원 행렬 출력: ')
print(mA); print(mB)
print()
print('행렬 합 출력: ')
print(mA + mB)
print('행렬 차 출력: ')
print(mA - mB)
print('행렬 곱 출력: ')
print(mA * mB)
print('행렬 나누기 출력: ')
print(mA / mB)

print()
print('각각의 2차원 행렬 출력: ')
data1 = [[1, 2, 3], [3, 2, 1]]
data2 = [[1, 2], [3, 4], [3, 1]]
print(data1); print(data2)

mA = np.array(data1)
mB = np.array(data2)
print('mA.dot(mB) 행렬 출력: ')
print(mA.dot(mB)) #수학의 행렬 곱 수행
print('np.matmul(mA, mB) 행렬 출력: ')
print(np.matmul(mA, mB)) #수학의 행렬 곱 수행
