data = '"홍길동",85'
data_list = data.split(',')
print(data_list)
data_list[0] = data_list[0].strip('"')
print('이름은 {}이고, 점수는 {}점 입니다.'.format(data_list[0],data_list[1]))