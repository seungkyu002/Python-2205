'''
    학생 클래스
        학생은 학번, 이름, 학과, 평점을 가지고 있다.
        핵생은 데이터를 셋팅하는 메서드, 학생 정보를 출력하는 메서드
        학생정보를 출력을 할때는 아래 형태처럼 출력
        평점 출력시 등급도 출력을 하게끔 하시오

        20211111    홍길동     컴퓨터공학과      3.45(B)
'''
class Student:
    def setting_data(self,sno,name,major,score):
        self.sno = sno
        self.name = name
        self.major = major
        self.score = score

    def get_grade(self):
        if self.score == 4.5:
            return 'A+'
        elif self.score >= 4.0:
            return 'A'
        elif self.score >= 3.5:
            return 'B+'
        elif self.score >= 3.0:
            return 'B'
        elif self.score >= 2.5:
            return 'C+'
        elif self.score >= 2.0:
            return 'C'
        elif self.score >= 1.5:
            return 'D+'
        elif self.score >= 1.0:
            return 'D'
        else:
            return 'F'

    def print_student_info(self):
        print(f'{self.sno}\t{self.name}\t{self.major}\t{self.score}({self.get_grade()})')
student = Student()
student.setting_data('2021111','홍길동','컴퓨터 공학과',3.45)
student.print_student_info()
