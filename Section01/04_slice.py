'''
    문자열 슬라이스
    형식
    문자열[begin : end : step]
        1) begin : 시작 인덱스, 포함, 생략하면 0부터 시작
        2) end : 종료 인덱스, 포함하지않음, 마지막 인덱스까지
        3) step : 증가/감소 값, 생략하면 1씩 증가
'''
#    01234567890
s = 'Hello_World'
print(s[0:6]) # Hello- 0번 인덱스 ~ 5번 인덱스
print(s[::]) # 전부 출력
print(s[0:8:2]) # 0 2 4 6 해당 인덱스 추출
print(s[:9]) # 0번 ~ 8번 인덱스 Hello_Wor
print(s[-4:]) # -4번 ~ -1번 인덱스
print(s[-9:-4]) #-9번 ~ -5번 인덱스

# 내장 함수 - len(문자열)
# len('Hello') --> 5 : 글자수를 구해주는 함수
print(len(s))

tel = '010-1234-5678'
# 전화번호 뒤에 4자리 추출해서 출력
print(tel[9:], tel[-4:])
# 전화번호 뒷자리 4자리만 제외하고 추출 010-1234-
print(tel[:9], tel[:-4])
print(tel[:len(tel)-4])