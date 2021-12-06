#%% 09-11plotbarh.py	가로 막대 그래프 그리기
import matplotlib.pyplot as plt

objects = ('Python', 'Java', 'C++', 'C#', 'C', 'Kotlin')
performance = [10, 8, 6, 4, 7, 2]

plt.title('Programming language usage') #제목
plt.xlabel('Usage') #x축 레이블
plt.ylabel('Programming language') #y축 레이블
plt.barh(objects, performance, height=0.5, color='yellow') #가로바 그리기
plt.show()
