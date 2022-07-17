'''
    섭씨를 화씨로 바꾸는 함수 - cel_to_fah
        섭씨 -> 화씨 : 섭씨온도 * 1.8 + 32
    화씨를 섭씨로 바꾸는 함수 - fag_to_cel
        화씨 -> 섭씨 : (화씨온도 - 32) / 1.8
'''
def cel_to_fah(cel):
    return cel * 1.8 + 32

def fah_to_cel(fah):
    return (fah - 32) / 1.8

cel = float(input('섭씨 온도를 입력하세요 >>>'))
print(cel_to_fah(cel))

fah = float(input('화씨 온도를 입력하세요 >>>'))
print(fah_to_cel(fah))