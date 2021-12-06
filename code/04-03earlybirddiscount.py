#%% 04-03earlybirddiscount.py	영화 조조 할인	판정
from time import localtime
hour = localtime().tm_hour
mnt = localtime().tm_min

#from datetime import datetime
#currunt = datetime.now()
#hour = currunt.hour
#mnt = currunt.minute
#n = int(input('지금 몇 시예요 ? '))

if hour < 10:
    print('지금 시각: %d시 %d분, 조조할인 됩니다. ' % (hour, mnt))
else: 
    print('지금 시각: %d시 %d분, 조조할인 안됩니다. ' % (hour, mnt))
