'''
    나이를 입력받은 다음에
    입력한 나이가 미성년자면 '미성년자' 출력
    입력한 나이가 성인이면 '성인' 출력
'''
a = int(input('나이 입력'))
# 방법1
if a >= 20:
    print('성인')
else:
    print('미성년자')

# 방법2
if a < 20:
    print('미성년자')
else:
    print('성인')