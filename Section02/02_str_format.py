name = '홍길동'
age = 20

# 이름 : 홍길동, 나이 : 20
print('이름 : '+name+', 나이 :'+str(age))
# format 함수
msg1 = '이름 : {}, 나이 : {}'.format(name,age)
msg2 = '이름 : {0}, 나이 : {1}'.format(name,age)
msg3 = '이름 : {1}, 나이 : {0}'.format(name,age)
print(msg1)
print(msg2)
print(msg3)

# 3.6버전 이상
msg4 = f'이름 : {name}, 나이 : {age}'
print(msg4)