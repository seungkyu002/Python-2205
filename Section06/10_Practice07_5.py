for i in range(1, 100):
    msg = ''
    if i >= 10 and i // 10 % 3 == 0:
        msg = '짝'
    if i % 10 in [3,6,9]:
        msg += '짝'
    if msg == '':
        print(i, end='\t\t')
    else:
        print(msg, end='\t\t')
    if i % 10 == 0:
        print()
