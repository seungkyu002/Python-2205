# 파일 열기 - 추가 모드, 추가모드도 파일이 없으면 자동생성
file = open('text.txt','at',encoding='UTF-8')
# 내용 추가
file.write('추가 텍스트\n')
# 파일 닫기
file.close()