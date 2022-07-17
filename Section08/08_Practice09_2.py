scores = []

while True:
    score = int(input('점수 입력 >>>'))
    if score < 0:
        break
    scores.append(score)

print(f'평균{sum(scores)/len(scores)},최대값={max(scores)},최소값{min(scores)}')