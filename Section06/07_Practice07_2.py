a=int(input('임의의 양수를 입력하세요 >>>'))
sum = 0
for i in range(a+1):
    sum += i
print('{}부터 {}사이 모든 정수의 합계는 {} 입니다.'.format(1,a,sum))