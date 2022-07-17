import csv

with open('차량관리.csv','wt',encoding='UTF-8',newline='') as file:
    csv_maket = csv.writer(file,delimiter=',',quotechar='"')
    csv_maket.writerow([1,'08러1234','2022-04-22 14:00'])
    csv_maket.writerow([2,'24가1114','2022-04-22 14:10'])
    csv_maket.writerow([3,'33우3222','2022-04-22 14:20'])
    csv_maket.writerow([4,'17호4443','2022-04-22 14:30'])
    csv_maket.writerow([5,'45로1253','2022-04-22 14:40'])
print('csv 파일이 생성되었습니다.')