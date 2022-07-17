'''
    학생 점수 5개를 입력 받은 후
    각 점수별 순위를 출력
    70, 90, 80, 70, 60

    1등 - 90
    2등 - 80
    3등 - 70
    3등 - 70
    5등 - 60
'''
lst = []
while len(lst) < 5:
    score = int(input('점수를 입력하세요 >>>'))
    if 0 <= score <= 100:
        lst.append(score)
    else:
        print('입력은 0~100사이의 정수만 입력하세요')

lst = sorted(lst,reverse=True)

for score in lst:
    rank = 1
    for s in lst:
        if score <s:
            rank += 1
        else:
            break
    print(f'{rank}등 - {score}점')