# 2~9단까지 구구단 출력

for dan in range(2,10):
    print('-----{}단-----'.format(dan))
    for i in range(1,10):
        print(f'{dan} * {i} = {dan * i}')