'''
    소멸자(Deconstructor)
        객체가 소멸되기 전에 자동으로 실행되는 메서드
'''
class Person:
    def __init__(self):
        print('생성자 호출')

    def __del__(self):
        print('소멸자 호출')

    def print_info(self):
        print('print_info')

p = Person()
s = Person()
del s
p.print_info()