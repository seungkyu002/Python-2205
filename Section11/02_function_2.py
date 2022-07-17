# 가변 매개변수, 받아온 데이터를 튜플로 관리
def printitem(*args):
    print(args)
    for item in args:
        print(item, end=' ')
    print()

printitem('Hello','Python','Welcome','Test')
printitem('홍길동')

# 매개변수에 기본값을 설정하는 디폴트값 매개변수
def printMessage(msg = '안녕하세요'):
    print(msg)
printMessage('한국에 오신것을 환영합니다.')
printMessage()

# 디폴트 값 설정시 주의할점
# 반드시 오른쪽 끝에서부터 설정(마지막 매개변수부터 연속적으로 저장)
# 인자값은 왼쪽부터 채우기 때문
def printNumbers(n1, n2=10):
    print(n1,n2)

printNumbers(20)