lst = ['서울','대전','대구','부산','제주']
# 목록 한건당 인덱스와 값을 튜플로 만들어서 꺼냄 -->(인덱스, 값)
for item in enumerate(lst):
    print(item)

# 목록 한건당 인덱스와 값을 따로 꺼냄
for index, item in enumerate(lst):
    print(index, item)

#-----------------------------------------------
print(list(range(10)))
print(list(range(0,10)))
print(list(range(0,10,2)))
print(tuple(range(0,10,2)))

# len(컬렉션) --> 저장되어 있는 데이터 개수
lst = list(range(10))
print(len(lst))
print(len(range(0,10,2)))

#------------------------------------------------
# 정렬
list1 = [5,1,45,23,437,56,3,22,51]
print(sorted(list1)) # 기본 설정은 오름차순으로 정렬
print(sorted(list1,reverse=True)) # 내림차순 정렬
print(sorted(list1,reverse=False)) # 오름차순 정렬

list2 = ['F','G','가','Z','a','A','B','E','z']
print(sorted(list2))
print(sorted(list2,reverse=True))
#------------------------------------------------
# zip - 각 리스트별 한개씩 튜플로 합쳐서 리턴
for item in zip(list1,list2):
    print(item)