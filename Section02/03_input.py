'''
    데이터 입력 받는 함수 : input
    input('화면에 출력할 내용')
    input 함수는 문자열로 입력 받기 때문에
    반드시 형변환 하는 작업이 필요
'''
name = input('이름을 입력하세요')
print('입력하신 이름 : {}'.format(name))

# 숫자 입력 해서 입력받은 숫자 출력

num = int(input('숫자 하나  입력하세요 >>>'))
print(num,type(num))

# 실수 입력 - float
r = float(input('원의 반지름 입력 :'))
print(r,type(r))