#%% Mini Project 4 13-04-scatterwithnumpy.py
import numpy as np
import matplotlib.pyplot as plt

SIZE = 30

x = np.arange(SIZE) #0, 1, 2, ..., 29
y = np.random.randint(0, 50, SIZE) #0 ... 50의 난수 30개
area = np.random.randint(10, 500, SIZE) #10 ... 500의 난수 30개
color = np.random.rand(SIZE) #0에서 1미만의 난수 30개

plt.scatter(x, y, s=area, c=color, alpha=0.4)
plt.xlabel('array x')
plt.ylabel('array y')
plt.show()
