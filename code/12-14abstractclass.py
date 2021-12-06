#%% 12-14abstractclass.py	추상 클래스를 상속 받아 추상 메소드를 구현 
from abc import *

class Polygon(metaclass = ABCMeta):
    @abstractmethod
    def area(self):
        print('면적 구하기 메소드 구현')

# poly = Polygon() #오류 발생
           
class Rectangle(Polygon):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self): #부모 클래스의 추상 메소드 구현
        return self.width * self.height

rect = Rectangle(2.4, 4.3)
print('사각형 면적: %.2f' % rect.area())