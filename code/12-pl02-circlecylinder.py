#%% 프로젝트 Lab 12-pl02-circlecylinder.py	원을 상속하여 원통을 구현
class Circle:
    ''' 원을 표현하는 클래스 정의 '''
    def __init__(self, radius = 1):
        self.radius = radius
            
    def area(self):
        return self.radius * self.radius * 3.14
    
class Cylinder(Circle):
    ''' 원통을 표현하는 클래스 정의 '''
    def __init__(self, radius, height):
        super().__init__(radius)
        self.height = height
            
    def volume(self): 
        ''' 원통 체적: 밑면인 원의 면적 × 높이 '''
        return super().area() * self.height
        
cy = Cylinder(3, 5)
print('원통 체적: %.2f' % cy.volume())