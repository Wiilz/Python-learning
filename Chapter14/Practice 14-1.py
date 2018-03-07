class BankAccount:
    def __init__(self,accountName ,accountNum):
        self.accountName = accountName
        self.accountNum =accountNum
        self.balance = 0.0
        
    def showBalance(self):
        print "Your account balance is",self.balance
        
    def saveMoney(self, money):
        self.balance = self.balance + money
        print "You deposit ",money
        print "Your new balance is ",self.balance

    def takeMoney(self, money):
        if self.balance >= money:
            self.balance = self.balance - money
            print "You withdraw",money
            print "Your new balance is",self.balance
        else:
            print "Your balance is not enough"
            print "Your balance is ",self.balance
            
myAccount = BankAccount("Warren","666666")
print "Account name :",myAccount.accountName
print "Account number :",myAccount.accountNum
myAccount.showBalance()
myAccount.saveMoney(20)
myAccount.takeMoney(10)
myAccount.takeMoney(10.2)
