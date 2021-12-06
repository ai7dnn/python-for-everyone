#%% 프로젝트 Lab 09-pl01-datetime.py	모듈 datetime 불러 날짜 계산
from datetime import date

#오늘부터 크리스마스까지 남은 일수 계산  
today = date.today() # 오늘 날짜
print('오늘: %d년 %d월 %d일' % (today.year, today.month, today.day))

xmasday = date(2019, 12, 25) #크리스마스 일 지정
delta = xmasday - today  #크리스마스까지 남은 일수를 계산
print('크리스마스까지 남은 일수: {}'.format(delta.days)) #남은 일수 출력

from datetime import timedelta

#오늘부터 100일 이후 날짜 출력 
date100 = timedelta(days = 100) #100일 후 지정
after100 = today + date100 #오늘 이후 100일 연산
print('오늘 이후 100일 이후 날짜: {}'.format(after100)) #오늘 이후 100일 출력 
