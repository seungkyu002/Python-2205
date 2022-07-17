filename = ''

while True:
    filename = input('복사할 파일명을 입력하세요 >>> ')
    if filename[-4:] == 'json':
        break
    print('복사할수 없는 파일입니다.')

with open(filename,'rt',encoding='UTF-8') as source:
    with open('복사본-'+filename,'wt',encoding='UTF-8') as copy:
        s = source.read()
        copy.write(s)
print('복사본-'+filename+' 파일이 생성되었습니다.')
