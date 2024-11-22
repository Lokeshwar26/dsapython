class bankacc:
    def __init__(self,__balance,__accno):
        self.__balance =__balance
        self.__accno=__accno
    def getaccno(self):
        return self.__accno
    def setaccno(self,newaccno):
        self.__accno=newaccno
    def getbalance(self):
        return self.__balance
    def deposit(self,amount):
        if amount > 0:
            self.__balance+=amount
            print(f"deposited{amount} and new balance is {self.__balance}")
        else:
            print(f"deposit the positive values")
    def withdraw(self,amount):
        if amount>0:
            if amount<=self.__balance:
                self.__balance-=amount
                print(f"{amount} has been withdrawn and remaining balanvce is{self.__balance}")
            else:
                print("insufficient funds")
        else:
            print("enter positive values")

account = bankacc(5000000,"12345678") 

print(f"Account number:{account.getaccno()}")
print(f"remaining balance in your account:{account.getbalance()}")

account.deposit(5000)
account.withdraw(6000)
account.deposit(-50)
account.withdraw(-90)
account.setaccno("987654321")
print(f"your updated account number is {account.getaccno()}")