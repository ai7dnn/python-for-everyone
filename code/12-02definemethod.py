#%% 12-02definemethod.py 클래스의 초기화 메소드와 일반 메소드 정의
class Singer:
    '''가수를 표현하는 클래스'''
    def __init__(self, name, debut):
        self.name = name
        self.debut = debut

    def introduce(self):
        print('안녕하세요! 가수 %s입니다.' % self.name)

    def age(self):
        print('데뷰한지 %d년이 되었네요.' % (2020 - self.debut + 1))

iyou = Singer('아이유', 2008)
iyou.introduce()
iyou.age()
