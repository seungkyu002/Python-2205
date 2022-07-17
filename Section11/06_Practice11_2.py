def vending_machine(money):
    a = 0
    while money >= 0:
        print(f'음료수 = {a}개, 잔고는 {money}원')
        money -= 700
        a += 1

vending_machine(3000)