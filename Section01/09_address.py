# 메모리 주소가 안바뀌는 형태
#mutable --> list, set, dict
lst = [1,2,3,4,5]
print(id(lst))
lst.append(100)
print(id(lst))
lst.remove(2)
print(id(lst))
print("----------------")
# 메모리 주소가 바뀌는 형태
# immutable --> int, float, str, tuple
num = 10
print(id(num))
num = 20
print(id(num))
newNum = num # num이 가지고 있는 주소를 newNum으로 저장
print(id(newNum))
