sec = int(input('초를 입력하세요 >>>'))
h = sec // 3600 # 시간
sec %= 3600
m = sec // 60 # 분
sec %= 60 # 초
print(f'변환 결과는 {h}시간 {m}분 {sec}초 입니다.')