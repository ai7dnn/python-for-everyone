#%% 04-01gradeif.py	평균평점 3.8이상이면 장학금 지급 대상자
grade = float(input('1학기 평균평점은? '))
if 3.8 <= grade:
    print('축하합니다! 장학금 지급 대상자입니다.')
print('당신의 1학기 평균평점 %.2f입니다.' % (grade))
