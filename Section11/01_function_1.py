'''
    함수(Function)
        자주 사용하는 기능을 내장함수 처럼 미리 만들어 놓은 코드
        사용자가 필요할 떄마다 불러서 쓴다.

    함수 문법
    def 함수명([매개변수, 매개변수....])
        실행할 코드 - 1
        실행할 코드 - 2
        ....
        [return 반환값]
'''
# 매개변수 X, 반환값 X
def printWelcome():
    print('Hello Python')
    print('Nice to meet you')

printWelcome()

# 매개변수 X, 반환값 O
def inputNumber():
    no = int(input('숫자 하나 입력 >>>'))
    return no

print(inputNumber() * 2)

# 매개변수 O, 반환값 x
def printPersonInfo(name,age):
    print(f'{name}님의 나이가{age}살 입니다.')

printPersonInfo('홍길동',20)
# 매개변수 개수 만큼 데이터를 보내지 않으면 에러
# printPersonInfo('홍길동')
# 매개변수 = 값, 순서가 달라도 매개변수 보낼 값을 매칭할 수 있다.
printPersonInfo(age=20,name='홍길동')

# 매개변수 O, 반환값 O
def sum(n1, n2):
    result = n1 + n2
    return result

print(sum(10,20))