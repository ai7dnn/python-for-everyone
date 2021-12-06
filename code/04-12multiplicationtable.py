#%% 04-12multiplicationtable.py	전형적인 구구단 출력
for i in range(2, 10):
    for j in range(1, 10):
        print('%d * %d = %2d' % (i, j, i * j), end= '  ')
    print()