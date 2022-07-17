a = int(input('4자리 사원번호를 입력하세요 >>>'))
msg = '오전' if a % 10 >= 5 else '오후'
print(msg)