import random as r
import time as t
pot = []
for i in range(1,46):
    pot.append(i)

jackpot = []
for i in range(6):
    r.shuffle(pot)
    pot.pop(len(pot)-1)
    jackpot.append(pot.pop(len(pot)-1))
    print('{}번째 당첨번호는 {}입니다.'.format(i+1,jackpot[-1]))
    t.sleep(2)
jackpot.sort()
print(f'이번 당첨번호는 {jackpot} 입니다.')