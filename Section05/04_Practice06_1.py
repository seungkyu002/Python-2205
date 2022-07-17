a = int(input('정수를 입력하세요. >>>'))
if a <= 0:
    print('잘못된 입력입니다.')
else:
    i = 0
    while i < a:
        print(f'{i+1}번째 Hello')
        i += 1