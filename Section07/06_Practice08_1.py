a = 10000
print(f'현재 {a}원 있습니다.')

while a != 0:
    m = int(input('사용할 금액 입력 >>>'))
    if m <= 0:
        print('0이하의 값은 입력할 수 없습니다.')
        continue
    if m > a:
        print(f'{m - a}원이 부족합니다.')
        continue
    a -= m
    print(f'현재 {a}원 있습니다.')
    if a == 0:
        break