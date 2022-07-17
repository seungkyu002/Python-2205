'''
    파일 모드
        r - 읽기, w - 쓰기, a - 추가, x - 배타적 추가
    파일 종류
        t - 텍스트 파일, b - 이진 파일

        wt ==> 쓰기 전용 텍스트 파일로 open
        rt ==> 읽기 전용 텍스트 파일로 open
'''
# 파일 열기
# 파일을 쓰기모드로 열고, 쓰기 모드로 열면 파일을 매번 새로 생성
# 파일 생성할때에는 파일경로에서 폴더는 미리 만들어져 있어야함, 폴더는 자동생성 X
#                       /test/firstFile.txt
# file = open(c:/test/firstfile.txt','wt',encoding='UTF-8)
file = open('/test/firstfile.txt','wt',encoding='UTF-8')
print('파일 오픈 완료')
print(file)
file.close() # 파일 닫기

with open('/test/secondFile.txt','wt',encoding='UTF-8') as file:
    print('파일 오픈 완료')
    print(file)
    #with 영억이 끝나면 자동으로 파일이 close 처리