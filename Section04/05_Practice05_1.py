a = int(input('점수를 입력하세요 >>>'))
# if a >= 90:
#     print('A')
# elif a >= 80:
#     print('B')
# elif a >= 70:
#     print('C')
# elif a >= 60:
#     print('D')
# else:
#     print('C')

#print('------------------------')

gr = 'F'
if a >= 90:
    gr = 'A'
elif a >= 80:
    gr = 'B'
elif a >= 70:
    gr = 'C'
elif a >= 60:
    gr = 'D'
print(f'점수는 {a}이고 학점은 {gr}입니다.')