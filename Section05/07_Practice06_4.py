s = set()

while len(s) < 5:
    a = (int(input('0~9사이 정수를 입력하세요. >>>')))
    if 0 <= a <= 9:
        s.add(a)
print('모두 입력되었습니다.')
print(f'입력된 값은 {s}입니다.')
