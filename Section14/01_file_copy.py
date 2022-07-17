# 파일 복사
# 원본 파일 --> 변수 --> 복사 파일
buffer_size = 1024

with open('strasbourg.jpg','rb') as source:
    with open('copy.jpg','wb') as copy:
        while True:
            buffer = source.read(buffer_size) # 원본에서 데이터 읽어옴
            if not buffer:
                break
            copy.write(buffer) # 읽어온 데이터를 새파일에 출력

print('파일 복사가 끝났습니다.')