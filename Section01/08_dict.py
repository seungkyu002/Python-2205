'''
    딕셔너리(dict) - dictionary
        데이터1 - 데이터2 한쌍으로 저장
        Key    - Value
        키값과 저장할 값이 한쌍으로 지정되서 저장
        키값을 이용해서 데이터를 읽기, 쓰고, 삭제, 수정
        키값은 중복이 안됨, 저장할 값은 중복이 됨
'''
# 딕셔너리 생성    Key:value
dict1 = {'홍길동':20,'김철수':33,'이영희':45}
# 딕셔너리에 저장된 값을 읽어옴
print(dict1['홍길동'])
# dict1['이영희'] = 777 데이터 수정
print(dict1['이영희'])
# print(dict1['김영희']) # 키값이 없으면 에러 발생
dict2 = dict(A = 'TEST', B = True)
print(dict2)
# 데이터 추가
dict1['김영희'] = 55
print(dict1)
dict1.setdefault('김용수',111)
print(dict1)
# 데이터 삭제
dict1.pop('김영희')
# dict1.pop('김영희') # 키값이 없으면 에러
print(dict1)
dict1.popitem() # 맨 마지막 키값에 해당하는 데이터를 삭제
print(dict1)