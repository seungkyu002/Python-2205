'''
    전역변수 : 함수 위치에 상관없이 어떤 함수에서도
              동일하게 접근이 가능한 변수
    지역변수 : 특정 영역에서만 접근이 가능한 변수
'''
age = 100 # 전역변수 - 함수 밖에 선언된 변수
def printA():
    print('printA :',age)
def printB():
    print('printB :',age)
age += 10
printA()
printB()

def printC():
    msg = 'Hello Python' # 지역변수로 선언, 함수가 끝나면 바로 사라짐
    print(msg)
printC()
# 외부에서는 printC에 있는 msg의 정체를 모른다
# print(msg)

if age < 200:
    abc = 'test' # if가 실행되었을때만 생성
print(abc)