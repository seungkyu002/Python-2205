basket = []
a = int(input('몇개의 과일을 보관할까요? >>>'))
for i in range(a):
    basket.append(input('{}번째 과일을 입력하세요 >>>'.format(i+1)))
print(f'입력받은 과일들은 {basket}입니다.')
