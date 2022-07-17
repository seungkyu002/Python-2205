# 시퀸스 연산자
lst1 = [1,2,3]
lst2 = [4,5,6]
lst3 = lst1 + lst2
print(lst3)
str1 = 'Hello'
str2 = 'World'
str3 = str1 + str2
str3 += '!!!!' # str3 = str3 + '!!!!'
print(str3)

# ---------------------------------
print('A' * 3)
print('A' * 4)
print('A' * 5)
print(lst1 * 2)

# 멤버십 연산자
# in , not in
print(10 in lst3) # 10이 lst3에 있냐?
print(10 not in lst3) # 10이 lst3에 없냐?
print('e' in str3) # e가 str3에 있냐?
print('e' not in str3) # e가 str3에 없냐?

# 삼항 연산자
# 조건식의 결과에 따라서 True일때 나타낼 식, False일때 나타낼 식
# (조건식의 결과가 참 일때 나타낼 연산식) if 조건식 slse (조건식의 결과가 거짓일때 나타낼 연산식)
n = 10
msg = '짝수' if n % 2 == 0 else '홀수'
print(msg)