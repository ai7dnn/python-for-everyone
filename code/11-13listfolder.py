#%% 11-13listfolder.py 현재 폴더 하부 목록 출력 
import os

dname = os.getcwd() #현재 폴더명을 저장
print('현재 폴더:', dname)

fs = os.listdir(dname) #현재 폴더의 하부 목록을 저장
for f in fs:
    if os.path.isfile(f): #파일 구분
        print('\t파일:', f)
    elif os.path.isdir(f): #폴더 구분
        print('\t폴더:', f)
