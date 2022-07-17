try:
    filename = input('열고자 하는 파일명을 입력하세요 >>>')
    file = open(filename,'rt',encoding='UTF-8')
except FileNotFoundError:
    print('{}파일이 존재하지 않습니다.'.format(filename))
else:
    buffer = file.read()
    print(buffer,end='')
    print()
    file.close()
finally: # Exception이 발생하든 안하든 무조건 마지막에 실행되는 영역
    print('프로그램을 종료합니다.')