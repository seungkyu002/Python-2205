dan = int(input('출력할 구구단을 입력하세요 >>>'))
for n in range(1,10): # range가 1 ~ 9 까지 숫자를 뽑음
    print('{} * {} = {}'.format(dan,n,dan*n))