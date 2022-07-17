import random as r

# 사용자로부터 로또번호 6개를 입력받음
# 단 중복된 숫자 X, 로또번호 범위 1~45

Lotto_set = set()
while len(Lotto_set) < 6:
    n = int(input('로또 번호를 입력하세요 >>>'))
    if n < 1 or n > 45:
        print('로또번호는 1~45 사이로 입력하세요')
        continue
    Lotto_set.add(n)
print('입력한 로또번호 목록 : {}'.format(Lotto_set))

# 로또 당첨 번호를 랜덤하게 뽑음 1~45 숫자들 중 7개 뽑음
# 마지막 번호는 보너스 번호
winning_Lotto_numbers = r.sample(range(1,46),7)
print('당첨된 로또번호 목록 : {}'.format(winning_Lotto_numbers))

# 당첨된 등수 및 낙첨 정보를 출력
count = 0
for i in range(len(winning_Lotto_numbers)-1):
    if winning_Lotto_numbers[i] in Lotto_set:
        count += 1
if count == 6:
    print('1등에 당첨 되셨습니다.')
elif count == 5 and winning_Lotto_numbers[-1] in Lotto_set:
    print('2등에 당첨 되셨습니다.')
elif count == 5:
    print('3등에 당첨 되셨습니다.')
elif count == 4:
    print('4등에 당첨 되셨습니다.')
elif count == 3:
    print('5등에 당첨 되셨습니다.')
else:
    print('낙첨 되셨습니다.')