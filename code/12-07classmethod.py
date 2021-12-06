# %% 12-07classmethod.py	클래스 메소드와 정적 메소드 정의와 활용
class Shape:
    PI = 3.141592  # 원주율, 클래스 변수 선언

    @classmethod
    def circlearea(cls, r):
        return r * r * cls.PI
        # return r * r * Shape.PI

    @staticmethod
    def circleperimeter(r):
        return 2 * r * Shape.PI

print('%.2f' % Shape.circlearea(3.2))
print('%.2f' % Shape.circleperimeter(3.2))

s = Shape()
print('%.2f' % s.circlearea(2.8))
print('%.2f' % s.circleperimeter(2.8))