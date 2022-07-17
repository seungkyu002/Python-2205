'''
    elif 조건식:
        실행문1
        실행문2
        ....
    elif는 if문으로 구성된 조건문에서
    두번째 조건문부터는 elif로 사용
'''
a = int(input('나이를 입력>>>'))
if a >= 20:
    print('성인')
elif a >= 17:
    print('고등학생 입니다.')
elif a >= 14:
    print('중학생')
elif a >= 8:
    print('초등학생')
else:
    print('미취학아동')