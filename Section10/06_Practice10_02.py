no = input('사업자등록번호를 입력하세요(예:123-45-67890) >>>')
no_list = no.split('-')
result = True

if len(no_list[0]) != 3 or len(no_list[1]) != 2 or len(no_list[2]) != 5:
    result = False

for n in no_list:
    if not n.isdecimal():
        result = False

if result:
    print('올바른 형식입니다.')
else:
    print('올바른 형식이 아닙니다.')