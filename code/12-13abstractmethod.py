#%% 12-13abstractmethod.py	추상 메소드 선언과 자식 클래스에서의 구현 
from abc import *

class Polygon(metaclass = ABCMeta):
    # pass
    @abstractmethod
    def area(self): #추상 메소드
        pass
            
class Triangle(Polygon):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self): #부모 클래스의 추상 메소드 구현
        return self.width * self.height / 2
    
tri = Triangle(2.4, 4.3)
print('삼각형 면적: %.2f' % tri.area())