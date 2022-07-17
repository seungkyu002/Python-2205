'''
    field : 클래스 구성요소 중에서 변수에 해당
    method : 클래스 구성요서 중에서 메서드(함수)에 해당

    Person 클래스
        저장할 데이터는 이름과 나이를 저장
        기능은 이름과 나이를 출력하는 print_person_info 메서드를 작성
'''
class Person:
    # self : 현재 생성된 객체
    def setting_data(self,name,age):
        # 필드 선언 방법 --> self.필드명 = 데이터
        self.name = name
        self.age = age

    def print_person_info(self):
        print(f'{self.name} - {self.age}')

person1 = Person()
person1.setting_data('홍길동',20)
person1.print_person_info()

# 이름 - 김철수, 나이 - 30 Person 객체를 생성하고
# 데이터 초기화 후 print_person_info

person2 = Person()
person2.setting_date('김철수',30)
person2.print_person_info()