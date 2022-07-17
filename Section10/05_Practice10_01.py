while True:
    t = input('전화번호를 입력하세요 >>>')
    if t.count('-') != 2:
        print('전화번호를 정확하게 - 포함해서 입력해 주세요')
        continue
    break
t_list = t.split('-')
print(t_list[1])