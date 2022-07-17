'''
    논리연산자 : 조건식이 두개 이상일때 처리하는 연산자
        and : 양쪽의 조건식이 둘다 True일때 True가 되는 연산자
        or : 양쪽의 조건식 중 하나라도 True면 True가 되는 연산자
        not : not 오른쪽에 있는 조건식의 결과를 반대로 뒤집는 연산자
              True면 False로, False면 True로 바꾸는 연산
'''
n1, n2 = 10, 7
print(n1 > 5 and n2 < 10) # True
print(n1 > 5 and n2 <7) # False
print(n1 > 5 or n2 <7) # True
print(n1 > 10 or n2 <7) # False
print(not n1 > 10) # True

# n1이 5보다 크고 n2가 10보다 작고 n1이 n2와 다르냐?
result = n1 > 5 and n2 < 10 and n1 != n2
print(result)