student_list = []

with open('학생정보.csv','rt') as file:
    student_list = file.readlines()
    for line in student_list:
        # print(line.replace('\n',''))
        arr = line.replace('\n','').split(",")
        for val in arr:
            print(val.strip('"'),end='\t')
        print()

        """
        car.csv 파일을 읽은 후 파일에서 4번째 데이터가 판매금액
        사용자로부터 입력 받은 금액 이상인 데이터만 출력
        """
        money = int(input('금액을 입력하세요 >>> '))
        with open('car.csv', 'rt') as file:
            while True:
                line = file.readline()
                if not line:
                    break
                line = line.replace('\n', '').split(',')
                if money <= int(line[3]):
                    print('{:20s} {:15s} {:4s} {:4s}'.format(line[0], line[1], line[2], line[3]))