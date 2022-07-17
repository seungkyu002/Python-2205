'''
    인덱스(index)
        1. 각 문자마다 부여된 번호
        2. 맨 앞에서부터는 0으로 번호가 시작
        3. 맨 뒤에서부터는 -1부터 번호가 시작
'''
s = 'Hello'
print(s[0], s[-5])
print(s[1], s[-4])
print(s[2], s[-3])
print(s[3], s[-2])
print(s[4], s[-1])
# s[2] = 'k' 부분수정 X

num = 100
#num을 문자열로 바꾸신 다음 한글자씩 출력
print(str(num)[0])
print(str(num)[1])
print(str(num)[2])