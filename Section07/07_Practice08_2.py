while True:
    a = int(input('영화 평점을 입력하세요 >>>'))
    if a < 1 or a > 5:
        print('평점은 1~5 사이만 입력할 수 있습니다.')
        continue
    print('평점 : {}'.format('★'*a))
    break