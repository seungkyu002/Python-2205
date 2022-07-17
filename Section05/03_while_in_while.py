'''
    숫자 하나를 입력받아서
    입력 받은 숫자에 해당하는 구구단 출력
'''
# dan = int(input('단 입력'))
# i = 1
# while i < 10:
#     print(f'{dan} * {i}= {dan * i}')
#     i += 1

# 2~9단 출력
dan = 2
while dan < 10:
    i = 1
    while i < 10:
        print(f'{dan} * {i}= {dan * i}')
        i += 1
    dan += 1
