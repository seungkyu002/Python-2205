a = int(input('정수1 입력 >>>'))
b = int(input('정수2 입력 >>>'))
c = int(input('정수3 입력 >>>'))
# 방법1
if a > b and a > c:
    print('가장 큰 수는 {}입니다.'.format(a))
elif b > a and b > c:
    print('가장 큰 수는 {}입니다.'.format(b))
else:
    print('가장 큰 수는 {}입니다.'.format(c))

# 방법2
# result = 0
# if a > b:
#     result = a
# else:
#     result = b
# if result < c:
#     result = c
# print('가장 큰 수는 {}입니다.'.format(result))

# 방법3
# result = a if a > b else b
# result = c if c > result else result
# print('가장 큰 수는 {}입니다.'.format(result))