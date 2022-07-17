a = input('비밀번호를 입력하세요 >>>')
ch_count = 0
num_count = 0
for ch in a:
    if ch.isalpha(): # 너 알파벳이냐? True or False
        ch_count += 1
    elif ch.isnumeric(): # 너 숫자냐? True or False
        num_count += 1
print(ch_count, num_count)
if ch_count > 0 and num_count > 0:
    print('가능한 비밀번호 입니다.')
else:
    print('불가능한 비밀번호 입니다.')