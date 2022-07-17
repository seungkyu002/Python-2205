print(chr(65)) # A
print(chr(66)) # B
print(chr(67)) # C
print(chr(90)) # Z
print(chr(97)) # a
print(chr(122)) # z
print(chr(32)) # space
print(chr(48)) # 0

# 알파벳 대문자와 소문자를 전부 출력
# A - a
# B - b
# ...
# Z - z
for i in range(65,91):
    print(f'{chr(i)} - {chr(i + 32)}')

# 문자를 유니코드 값으로 변환
print(ord('A'),ord('a'))
print(ord('가'),ord('힣'))\

# eval : 문자열 값이 연산식이면 해당 연산으로 연산식을
#        계산해서 결과값을 리턴
print(eval('100+200'))
a = 10
print(eval('a * 10'))
print(eval('min(4,3,2,6,1,5,3,2,0)'))

print(format(1000000))
print(format(1000000,','))
print(format(1000000,'_'))
#-----------------------------------------
print(str(100)+'Hello')