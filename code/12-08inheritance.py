# %% 12-08inheritance.py	부모 클래스와 자식 클래스 정의와 활용
class Robot:
    def __init__(self):
        self.laws = '인간에게 해를 입혀서는 안됩니다.'

    def hello(self):
        print('전 로봇입니다.')

    def __str__(self):
        return '전 로봇으로 ' + self.laws

class HumanoidRobot(Robot):
    def __init__(self, name):
        # super().__init__()
        self.name = name

    def speak(self):
        print('%s는 사람처럼 말을 할 수 있습니다.' % self.name)

roboi = Robot()
print(roboi)

hr = HumanoidRobot('아시모')
hr.hello()
hr.speak()
# print(hr)
# print(hr.laws) #오류 발생