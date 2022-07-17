# 절대값 구하는 함수
print(abs(10),abs(-10))

# 몫과 나머지를 구하는 함수 - 결과는 튜플로
print(divmod(10,7)) # 몫 - 1, 나머지 - 3

lst = [119,12,23,45,65,21,44]
# 최대값
print(max(lst),max(119,12,23,45,65,21,44))
# 최소값
print(min(lst),min(119,12,23,45,65,21,44))
# 거듭제곱
print(2 ** 10, pow(2,10))
# 총합 - 숫자만 사용가능, 숫자가 아닌 값이 들어가면 에러처리
print(sum(lst))
# 반올림
print(round(156.123456,0))
print(round(156.123456,1))
print(round(156.123456,2))
print(round(156.123456,4))
print(round(156.123456,-1))
print(round(156.123456,-2))