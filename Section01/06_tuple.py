'''
    튜플(tuple)
        데이터를 리스트와 동일한 형태로 저장
        데이터를 읽는 방식도 리스트와 동일
        단, 최초에 저장한 데이터만 유지
        튜플에서는 데이터를 추가, 삭제, 수정할 수 없다.
'''
# 튜플 생성
tup1 = (1, 41, 'Hello', False, True, 3.1415)
print(tup1)
print(type(tup1))
tup2 = 1, 41, 'Hello', False, True, 3.1415
print(tup2)
lst = [1,2,3,4,5]
# 리스트를 가지고 튜플로 생성
tup3 = tuple(lst)
print(tup3)
# 튜플를 가지고 리스트로 생성
lst2 = list(tup1)
print(lst2)
# 튜플에 있는 데이터 접근은 인덱스를 이용함
print(tup1[0],tup1[3])
print(tup1[0:3])
# tup1[0] = 100 # 튜플은 값 수정이 안됨


# 튜플 수정 방법
# 리스트로 변경 -> 데이터 추가 -> 다시 튜플로 변경
'''
lst3 = list(tup1)
print(lst3)
lst3.append('Append')
print(lst3)
tup4 = tuple(lst3)
print(tup4)
'''
