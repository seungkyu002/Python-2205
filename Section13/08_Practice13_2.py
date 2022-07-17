with open('연락처.txt','rt',encoding='UTF-8') as file:
    line_list = file.readlines()
    count = 0
    idx = 0
    for line in line_list:
        arr = line.split(",")
        tel = arr[2]
        if tel[:3].count('011') == 1:
            tel = tel.replace('011','010')
            count+=1
            arr[2] = tel
            line_list[idx] = ",".join(arr)
        idx += 1
    print(line_list)

with open('연락처.txt','wt',encoding='UTF-8') as file:
    for line in line_list:
        file.write(line)
print(f'총 {count}건의 011 데이터를 찾았습니다.')
print('모든 데이터를 수정했습니다.')