# r = ['red','orange','yellow','green','blue','navy','purple']
# for a,b in enumerate(r,start=1):
#     print(f'무지개의 {a}번째 색은 {b}입니다.')


r = ['red','orange','yellow','green','blue','navy','purple']
for index, value in enumerate(r):
    print(f'무지개의 {index+1}번째 색은 {value}입니다.')