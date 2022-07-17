for dan in range(2,10):
    if dan % 2 == 0:
        continue
    for i in range(1,10):
        print(f'{dan} * {i} = {dan*i}')
        if dan == i:
            break
    print()