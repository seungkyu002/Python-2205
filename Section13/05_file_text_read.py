# 파일 열기 _ 읽기 모드에서 파일이 반드시 있어야됨, 없으면 에러 발생
file = open('text.txt','rt',encoding='UTF-8')
# 텍스트 읽어오기
content = file.read()
print(content)
file.close()
print('------------------------------------')
file = open('text.txt','rt',encoding='UTF-8')
while True:
    content = file.readline() # 한줄씩 읽어옴
    if not content:
        break
    print(content,end='')
file.close()
print('------------------------------------')
file = open('text.txt','rt',encoding='UTF-8')
#파일 내용을 전부 읽어와서 한줄 단위로 리스트 생성
line_list = file.readlines()
#print(line_list)
for line in line_list:
    print(line,end='')
file.close()
