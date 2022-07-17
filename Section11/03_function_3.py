# 다중 반환
# , ----> 리턴시 데이터 및 변수를 구분

def return_mulit(*args):
    return sum(args), sum(args)/len(args), max(args), min(args)

result = return_mulit(1,2,3,4,5,6,7,8,9,10)
print(result)
# 리턴 값 개수에 맞춰서 받음(개수 안맞으면 에러)
s, a, m, n = return_mulit(1,2,3,4,5,6,7,8,9,10)
print(s, a, m, n)