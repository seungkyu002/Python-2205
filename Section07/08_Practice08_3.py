# count = 5
# while count > 0:
#     a = input('비밀번호를 입력하세요 >>>')
# 
#     if a == 'qwerty':
#         print('비밀번호를 맞췄습니다.')
#         break
# 
#     count -= 1
# 
# if count == 0:
#     print('비밀번호 입력 횟수를 초과했습니다.')

# print('-----------------------------------------------')

result = False
for i in range(5):
    paw = input('비밀번호를 입력하세요 >>>')
    
    if paw == 'qwerty':
        result = True
        break
        
if result:
    print('비밀번호를 맞췄습니다.')
else:
    print('비밀번호 입력 횟수를 초과했습니다.')