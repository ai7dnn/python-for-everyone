#%% 12-09superoveriding.py	내장 함수 super()의 사용과 메소드 오버라이딩
class Singer:
    def __init__(self, name, debut):
        self.name = name
        self.debut = debut
        
    def introduce(self):
        print('안녕하세요! 가수 %s입니다.' % self.name)        

    def age(self):
        print('데뷰한지 %d년이 되었네요.' % (2020 - self.debut + 1))    

class KPopGroup(Singer):
    def __init__(self, name, debut, cnt):
        # super().__init__(name, debut) #부모의 초기화 메소드 호출
        self.name = name
        self.debut = debut
        self.cnt = cnt
        
    def introduce(self): #메소드 오버라이딩
        super().introduce()     
        print('우린 KPop 그룹으로 %d명 입니다.' % self.cnt)        

bts = KPopGroup('BTS', 2013, 7)
bts.introduce()
bts.age()