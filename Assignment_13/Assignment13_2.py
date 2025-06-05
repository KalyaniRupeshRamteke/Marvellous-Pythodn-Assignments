class BankAccount:
    ROI = 10.5

    def __init__(self,name,amount):
        self.Name = name
        self.Amount = amount

    def Deposite(self,amt):
        self.Amount = self.Amount + amt
    
    def Withdraw(self,amt):
        self.Amount = self.Amount - amt
    
    def calculateIntrest(self):
        intrest = 0
        intrest = (self.Amount * BankAccount.ROI * 1) / 100
        return intrest

    def Display(self):
        print(self.Name," ==>",self.Amount,end = " ")
        print("\n")

def main():

    bankAcnt = BankAccount("Kalyani",10000)
    print("Initially")
    bankAcnt.Display()
    print("After Deposite Amount")
    bankAcnt.Deposite(1000)
    bankAcnt.Display()
    print("After withdraw amount")
    bankAcnt.Withdraw(500)
    bankAcnt.Display()
    intAmt = bankAcnt.calculateIntrest()
    print("Intrest amount based on amount is :",intAmt)


    bankAcnt = BankAccount("Rupesh",15000)
    print("Initially")
    bankAcnt.Display()
    print("After Deposite Amount")
    bankAcnt.Deposite(2000)
    bankAcnt.Display()
    print("After withdraw amount")
    bankAcnt.Withdraw(1500)
    bankAcnt.Display()
    intAmt = bankAcnt.calculateIntrest()
    print("Intrest amount based on amount is :",intAmt)


if __name__ == "__main__":
    main()
