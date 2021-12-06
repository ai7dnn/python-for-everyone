#%% 12-06staticmethod.py	정적 메소드로 섭씨와 화씨 간의 온도 변환
class Degree:
    @staticmethod
    def tofahrenhite(celsius):
        return celsius * 1.8 + 32

    @staticmethod
    def tocelcius(fahrenhite):
        return (fahrenhite - 32) / 1.8

print('%.2f' % Degree.tofahrenhite(30))
print('%.2f' % Degree.tocelcius(100))

d = Degree()
print('%.2f' % d.tofahrenhite(35))
print('%.2f' % d.tocelcius(90))