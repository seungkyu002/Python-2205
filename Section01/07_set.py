'''
    세트(set)
        집합 형태의 자료형
        1. 중복된 데이터가 저장될 수 없음 --> 고유값만 저장
        2. 데이터가 자동 정렬 --> 저장되는 순서가 보장되지 않음
'''
# set 생성
set1 = {3,5,1,2,7,2,1,3,7,-3,11}
print(set1)
lst = [1,1,1,1,5,23,1,34,3]
set2 = set(lst)
print(set2)
tup = (3,4,1,2,2,1,5,4)
set3 = set(tup)
print(set3)
# 데이터 추가
set1.add(10)
set1.add(20)
set1.add(20)
print(set1)
# 데이터 삭제
set1.remove(5)
# set1.remove(5) 삭제할 데이터가 없으면 런타임 에러로 처리
print(set1)
set1.pop()
print(set1)
set1.discard(10)
set1.discard(10) # 삭제할 데이터가 없어도 에러로 처리하지 않음
print(set1)