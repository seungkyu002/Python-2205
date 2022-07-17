'''
    변수(variable)
        데이터를 하나 저장할 공간
'''
# box라는 이름으로 메모리 공간을 하나 만들고
# 그 공간에 데이터 10을 저장
box = 10
# 변수 오른쪽에 =이 없으면 계산하는 값 용도로 쓰임
# 이 때는 저장하는 용도가 아니라서 변수가 저장하고 있는 값을 읽어옴
print(box)
box = 20
box = 30
print(box) # 30마지막에 저장된 값을 읽어옴
t = 100
print(box + t) # t에 저장된 값과 box에 저장한 값을 읽어와서 더함
result = box + t
print(result)
# box에 값을 바꿔도 result는 변함이 없다.
# result에는 계산한 결과값만 저장되어 있음
box = 200
print(result)

'''
    변수명 짓는 규칙
        1. 알파벳, _, 숫자
        2. 대소문자 구분
        3. 변수명 중복X
        4. 변수명 첫글자에는 숫자를 쓸 수 없음
        5. 키워드와 변수명이 동일하면 안됨
        6. 한글 및 기타 언어들을 변수명으로 추천하지 않음
'''
name = '정승규'
num = 20
pi = 3.1415
flag = True
print(name, type(name))
print(num, type(num))
print(pi, type(pi))
print(flag, type(flag))
name = 100
print(name, type(name))