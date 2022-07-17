'''
    생성자(Constructor)
        객체를 생성할 때 제일 먼저, 단 한번만 실행되는 메서드
'''
class Person:
    def __init__(self):
        print('Person 생성자')
        self.name='홍길동'
        self.age = 20

    def print_info(self):
        print(f'{self.name} - {self.age}')

p1 = Person()
p2 = Person()
p3 = Person()
p1.print_info()
p2.print_info()
p3.print_info()

class Animal:
    #생성자에 매개변수를 선언하면 해당 클래스 생성시
    #반드시 매개변수에 해당하는 인자값을 넣어줘야됨
    def __init__(self, age):
        self.age = age

    def print_info(self):
        print(f'동물의 나이 {self.age}')
#생성자에서 매개변수가 있기때문에 반드시 해당하는 값을 넣어줘야됨
animal = Animal(20)
animal.print_info()





