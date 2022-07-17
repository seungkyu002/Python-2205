# 정렬
print('10자리 폭 오른쪽 정렬 : {:>10d}'.format(123))
print('10자리 폭 오른쪽 정렬 : {:>10s}'.format('A'))
print('10자리 폭 오른쪽 정렬 : {:>10s}'.format('가'))

print('10자리 폭 왼 쪽 정렬 : {:<10d}'.format(123))
print('10자리 폭 왼 쪽 정렬 : {:<10s}'.format('A'))
print('10자리 폭 왼 쪽 정렬 : {:<10s}'.format('가'))

print('10자리 폭 가운데 정렬 : {:^10d}'.format(123))
print('10자리 폭 가운데 정렬 : {:^10s}'.format('A'))
print('10자리 폭 가운데 정렬 : {:^10s}'.format('가'))
# 빈공간을 *로 채움(빈공간을 채우는 문자는 하나만 허용)
print('10자리 폭 왼 쪾 정렬 채움문자 : {:*<10d}'.format(123))
print('10자리 폭 오른쪾 정렬 채움문자 : {:*>10s}'.format('A'))
print('10자리 폭 가운데 정렬 채움문자 : {:*^10s}'.format('가'))

s = 'Hello World Test World In Python'
print(s.count('World')) # World의 개수
print(s.count('World',12)) # 인덱스 12부터 World의 개수
print(s.find('World')) # 처음부터 World가 있는 위치를 찾음
print(s.find('World',12)) # 인덱스 12부터 검색, World가 있는 위치
print(s.find('World',22)) # 찾는 문자열이 없으면 -1을 리턴함
print(s.rfind('World')) # 끝에서부터 World가 있는 위치를 찾음
print(s.index('World')) # 처음부터 World가 있는 위치를 찾음
print(s.index('World',12)) # 인덱스 12부터 검색, World가 있는 위치
#print(s.index('World',22)) # 찾는 데이터가 없으면 에러로 처리함

#--------------------------------------------------------------
print(s.upper()) # 전부 대문자로 변환
print(s.lower()) # 전부 소무자로 변환
print(s.capitalize()) # 첫글자만 대문자로, 나머지는 소문자로 변환

#--------------------------------------------------------------
lst = ['A','3','Z','B','4']
print('+'.join(lst)) # 리스트의 각 요소들을하나의 문자열로 합쳐줌, 데이터 사이에 +로 연
l = 'A+3+Z+4'
split_list = l.split('+') # 특정 문자열을 기준으로 문자열을 쪼갬, 쪼갠 문자열을 리스트로
print(split_list)

#--------------------------------------------------------------
print(s.replace('World','Hell'))

s1='                           A'
s2='A                           '
s3='             A              '

print(s1.lstrip()),len(s1.lstrip()) # 왼쪽에 있는 공백을 전부 제거
print(s2.rstrip()),len(s2.rstrip()) # 오른쪽에 있는 공백을 전부 제거
print(s3.strip()),len(s3.strip()) # 좌우에 있는 공백을 전부 제거

s1 = '.....A'
print(s1.lstrip('.')) # 왼쪽부터 연속된 .을 제거