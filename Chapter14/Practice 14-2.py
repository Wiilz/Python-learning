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

class InterestAccount(BankAccount):
    def __init__(self,accountName ,accountNum,rate):
        BankAccount.__init__(self,accountName ,accountNum)
        self.rate = rate
    def addInterest(self):
        interest = self.balance + self.balance * self.rate
        print"adding interest  to the account,",self.rate * 100, "percent"
        self.saveMoney(interest)
            
myAccount = InterestAccount("Warren","666666",0.11)
print "Account name :",myAccount.accountName
print "Account number :",myAccount.accountNum
myAccount.showBalance()
myAccount.saveMoney(20.66)
myAccount.addInterest()
