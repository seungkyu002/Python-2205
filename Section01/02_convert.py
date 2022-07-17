'''
    데이터 형변환 --> 데이터 타입을 다른 데이터 타입으로 변경
    1. 정수로 형변환 - int(데이터 또는 변수)
        -int(1.9) --> 소수점 제가 ->1
        -int('200') --> 문자열을 숫자로 변환 -->
        -int('3.1415') --> 에러발생(문자열  내용이 정수가 아니다)
        -int(True) --> 1
        -int(False) --> 0
'''
print(int(1.9))
print(int('200'))
# print(int('3.1415'))
print(int(True))
print(int(False))
'''
    2. 실수로 형변환
        -float(20) --> 20.0
        -float('3.1415') --> 3.1415
        -float('20') --> 20.0
        -float(True) --> 1.0
        -float(False) -->0.0
'''
print(float(20))
print(float('3.1415'))
print(float('20'))
print(float(True))
print(float(False))
'''
    3. 문자열 변환 - str(데이터 및 변수)
        - str(111)
        - str(3.1415)
        - str(True)
'''
print(str(111))
print(str(3.1415))
print(str(True))
'''
    4. 논리값으로 형변환 - bool(데이터 및 변수)
        -bool(0) --> False
        -bool(1) --> True
        -bool(-1) --> True
        -bool('hello') --> True
        -bool('') --> False
'''
print(bool(0))
print(bool(1))
print(bool(-1))
print(bool('hello'))
print(bool(''))