class Bankaccount:
     def __init__(self):
        self._balance=1000
     def deposit(self,amount):
        self._balance+=amount
     def withdraw(self,amount):
        if amount<=self._balance:
           self._balance-=amount
        else:
           print("insufficient balance")
     def get_balance(self):
        return self._balance
s1=Bankaccount()
print(s1.get_balance())
s1.deposit(500)
print(s1.get_balance())
s1.withdraw(2000)
print(s1.get_balance())


