try:
    n1 = int(input('숫자 입력 >>>'))
    n2 = int(input('숫자 입력 >>>'))
    print(n1/n2)
except ValueError as e1:
    print(e1)
except ZeroDivisionError as e2:
    print(e2)

print('프로그램 종료')