# 파일 열기
file = open('text.txt','wt',encoding='UTF-8')
# 텍스트 출력
file.write('안녕하세요\n')
file.write('Hello World')
# 파일 닫기
file.close()