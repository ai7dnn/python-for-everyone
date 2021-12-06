# %% 12-04clsinstattribute.py	클래스와 인스턴스 속성 활용
class Rectangle:
    ''' 사각형을 표현하는 클래스 정의 '''
    count = 0  # 클래스 속성(class attribute)

    def __init__(self, width, height):
        self.width = width  # 인스턴스 속성 참조
        self.height = height  # 인스턴스 속성 참조
        Rectangle.count += 1  # 클래스 속성 참조

    def __str__(self):
        return '사각형 가로: {} 세로: {}'.format(self.width, self.height)


r1 = Rectangle(2.3, 3.2)
r2 = Rectangle(1.4, 2.8)
print(r1)
print(r2)
print(Rectangle.count, r1.count, r2.count)
