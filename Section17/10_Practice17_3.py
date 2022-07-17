class BankError(Exception):
    def __init__(self,message):
        super().__init__(message)

class BankAccount:
    def __init__(self,acc_no,balance):
        self.acc_no = acc_no
        self.balance = balance

    def inquiry(self):
        print(f'계좌번호 : {self.acc_no}')
        print(f'통장잔액 : {self.balance}')

    def deposit(self,money):
        if money <= 0:
            raise BankError('{}원 입금불가'.format(money))
        self.balance += money

    def withdraw(self,money):
        if money <= 0:
            raise BankError('{}원 출금불가'.format(money))
        elif self.balance < money:
            raise BankError('{}원 잔액부족'.format(money-self.balance))
        self.balance -= money

    def transfer(self,you_acc,money):
        if money <= 0:
            raise BankError('{}원 이체불가'.format(money))
        elif self.balance < money:
            raise BankError('{}원 잔액부족'.format(money-self.balance))
        you_acc.deposit(money)
        self.balance -= money


me = BankAccount('012-34-56789',50000)
your = BankAccount('987-65-43210',50000)
try:
    me.transfer(your,50000)
except BankError as e:
    print(e)
finally:
    me.inquiry()
    your.inquiry()