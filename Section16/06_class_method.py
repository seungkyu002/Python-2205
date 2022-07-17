class Count:
    class_count = 0#클래스 변수, 인스턴스들 끼리 공유하는 변수

    @classmethod
    def add_count(cls):
        #cls에서는 객체(self)가 가지고 있는 값 메서드에 접근이 불가능
        cls.class_count += 1

    def __init__(self):
        #생성자나 메서드에서 클래스 변수나 메서드에 접근 할려면 클래스명으로 접근 가능
        Count.class_count += 1
        print(f'생성자 {Count.class_count}')

    @staticmethod
    def static_method():
        #클래스 메서드나 변수에 직접 접근이 불가능
        print('인스턴스 생성 없이 사용이 가능한 메서드')
        Count.class_count += 1

Count.add_count()
print(Count.class_count)
c1 = Count()
c2 = Count()
c1.add_count()
c2.add_count()
print(Count.class_count)
Count.static_method()