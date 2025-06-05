class BankAccount:

    def __init__(self,accountNum,name,balance):
        self.AccNo = accountNum
        self.Name = name
        self.Balance = balance

    def Deposite(self,amount):
        self.Balance = self.Balance + amount
        return self.Balance

    def Withdraw(self,amount):
        if(amount >  self.Balance):
            print("No sufficient balance for withdraw")
        else:
            self.Balance = self.Balance - amount
        
        return self.Balance

    def Display(self):
        print("Account Number",self.AccNo)
        print("Name:",self.Name)
        print("Balance:",self.Balance)

def main():

    obj = BankAccount(111,"Kalyani",1000)

    print("initially Balance")
    obj.Display()

    obj.Deposite(1000)
    print("After deposite amount")
    obj.Display()

    obj.Withdraw(2500)
   
    obj.Withdraw(500)
    print("After withdraw amount")
    obj.Display()

if __name__ == "__main__":
    main()
    