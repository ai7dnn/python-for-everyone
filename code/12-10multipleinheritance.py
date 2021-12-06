#%% 12-10multipleinheritance.py	다중 상속 구현
class Student():
    def study(self):
        print('공부하는 학생입니다.')

class Employee():
    def work(self):
        print('일하는 직원입니다.')

class Assistant(Student, Employee):
    def do(self):
        self.study()
        self.work()

i = Assistant()
i.do()        