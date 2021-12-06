# %% 12-03magicmethod.py	더블 언더스코어가 붙은 특수 메소드
class Circle:
    ''' 원을 표현하는 클래스 정의 '''

    def __init__(self, radius=1):
        self.radius = radius

    def __str__(self):
        return '원 반지름: {}'.format(self.radius)

    def __eq__(self, other):
        if self.radius == other.radius:
            return True
        else:
            return False

    def setradius(self, radius):
        self.radius = radius

    def getradius(self):
        return self.radius

    def area(self):
        return self.radius * self.radius * 3.14

    def perimeter(self):
        return 2 * self.radius * 3.14


c1 = Circle(10)
print('원 반지름: %.2f' % c1.getradius())
print('원 면적: %.2f' % c1.area())
print('원 둘레: %.2f' % c1.perimeter())
print(c1)

c2 = Circle()
c2.setradius(20)
c3 = Circle(10)
print(c1 == c2)
print(c1 == c3)
