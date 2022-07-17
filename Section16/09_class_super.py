class Animal:
    def __init__(self, age):
        self.age = age
        print('Animal 생성자 호출')

    def print_info(self):
        print('이 동물의 나이 : {}'.format(self.age))

class Person(Animal):
    def __init__(self,age,name):
        #자식 생성자는 부모 클래스 생성 필요한 데이터를 받아서 보내줘야됨
        super().__init__(age)
        self.name = name
        print('Person 생성자 호출')
    def print_info(self):
        print('이름 : {}'.format(self.name))
        print('나이 : {}'.format(self.age))
        super().print_info()

p = Person(20,'홍길동')
p.print_info()