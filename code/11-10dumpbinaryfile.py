#%% 11-10dumpbinaryfile.py	다양한 파이썬 자료형을 바이너리 파일로 출력  
import pickle as pk 

month = {1: 'January', 2: 'February', 3: 'March', 4: 'April'}
month[5] = 'May'
month[6] = 'June'
lst = ['pascal', 'python', 'java']

#바이너리 파일 쓰기
with open('dicmonth.pic', mode='wb') as f:
    pk.dump(month, f)
    pk.dump(lst, f)

print(' 바이너리 파일 쓰기 완료! '.center(30, '*'))
