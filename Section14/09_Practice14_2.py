import csv

with open('cctv (1).csv','rt',newline='') as file:
    csv_reader = csv.reader(file)
    count = 0
    for line in csv_reader:
        if line[4].isdecimal():
            count += int(line[4])
print('����� �������� ��ġ�� cctv�� �� {}�� �Դϴ�'.format(count))