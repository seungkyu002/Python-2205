a = int(input('자판기에 얼마를 넣을까요? >>>'))
b = 0
while a >= 300:
    b += 1
    a -= 300
    print(f'커피{b}잔, 잔돈{a}원')