#%% 12-01defsimpleclass.py	간단한 클래스의 정의와 활용
class Person:
    '''사람을 표현하는 클래스'''

def hello(p):
    print('%s이 인사합니다.' % p.name)

Person.hello = hello

he = Person()
he.name = '홍길동'
he.age = 20
print(he.name, he.age)
he.hello()
print(isinstance(he, Person))

she = Person()
she.name = '신입생'
she.age = 19
print(she.name, she.age)
she.hello()
print(isinstance(she, Person))