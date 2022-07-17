'''
    리스트(list)
        데이터를 원하는 만큼 여러개 데이터를 순서대로 저장
        1. 중복된 데이터를 저장할 수 있음
        2. 데이터를 추가한 순서대로 저장
        3. 데이터를 추가, 삭제, 수정이 가능
'''
# 리스트 생성
#      0 1  2      3    4      5
lst = [1,2,'Hello',True,False,'World']
print(lst)
# 리스트도 인덱스 번호를 이용해서 데이터를 하나씩 뽑을 수 있음
print(lst[0])
print(lst[3])
print(lst[5])
print(lst[-1])
print(lst[-5])
# print(lst[6]) 인덱스 범위 초과 에러
print('------------')
# 리스트 1번 인덱스 부터 3번 인덱스까지 추출
print(lst[1:4], lst[-5:-2])
extract_list = lst[1:4]
print(extract_list)
print(lst)

# 추가, 삭제, 수정
# 리스트에 데이터 추가, 맨뒤에 추가됨
lst.append('Append')
print(lst)
# 3번 인덱스에 데이터를 끼워넣기, 한칸씩 뒤로 밀림
lst.insert(3,777)
print(lst)
# 수정
lst[3] = 100
print(lst)
# 삭제
# pop은 인덱스 번호에 해당하는 데이터를 삭제
# 인덱스 번호를 생략하면 맨 마지막 데이터를 삭제
lst.pop()
print(lst)
lst.pop(2)
print(lst)
# remove 일치하는 데이터를 기준으로 삭제
# 맨처음 검색 되는 첫번째 데이터만 삭제
lst.remove(True)
print(lst)
print(len(lst)) # 데이터 개수 체크
# 전체 삭제
lst.clear()
print(lst)