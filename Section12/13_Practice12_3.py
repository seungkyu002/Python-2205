import random as r
win = 0
draw = 0
lose = 0
lst = ['바위','가위','보']

for i in range(5):
    p = int(input('바위-1,가위-2,보-3 입력 >>>'))
    com = r.randrange(1,4)
    if p % 3 + 1 == com:
        win += 1
        msg = '당신이 이겼습니다.'
    elif p == com:
        draw += 1
        msg = '비겼습니다.'
    else:
        lose +1
        msg = '컴퓨터가 이겼습니다.'
    print(f'당신은 {lst[p-1]}선택, 컴퓨터는 {lst[com-1]}, {msg}')
print(f'당신의 전적은 : 승 : {win}, 무 : {draw}, 패 {lose}')