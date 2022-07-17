'''
    비트 연산자 : 비트 단위로 계산하는 연산자
                &  ----->  and
                |  ----->  or
                ^  ----->  xor
                ~  ----->  not
            >> <<  ----->  shift
'''
n1 = 10 # 1010
n2 = 7  # 0111
print(n1 & n2)
print(n1 | n2)
print(n1 ^ n2)
print(~n1)
n3 = 1
print(n3 << 1)
print(n3 << 2)
print(n3 << 3)
print(n3 >> 1)
print(n3 >> 2)
print(n3 >> 3)
n4 = -11
print(n4 >> 3)
print(n4 << 3)