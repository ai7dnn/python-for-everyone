#%% Mini Project 3 13-03-scattergraph.py
import matplotlib.pyplot as plt
import random as r

x = list(range(10))
y = [r.randint(1,10) for _ in range(10)]
area = [r.randint(10, 100) for _ in range(10)]
color =  [r.random() for _ in range(10)]

plt.scatter(x, y, s=area, c=color)
plt.show()
