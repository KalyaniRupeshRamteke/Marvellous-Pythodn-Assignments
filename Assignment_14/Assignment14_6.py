class Calculator:

    #def __init__(self,num,num2):
    #   self.val1= num
    #    self.val2=num2

    def Addition(self,a,b):
        res = 0
        res = a + b
        return res

    def Substraction(self,a,b):
        res = 0
        res = a - b
        return res
    
    def Multiplication(self,a,b):
        res = 0 
        res = a*b 
        return res 
    
    def Division(self,a,b):
        res = 0
        res = a/b
        return res

def main():

    print("Enter 2 values for arithmatic calculation")

    x = int(input())
    y = int(input())

    obj = Calculator()

    sum = obj.Addition(x,y)
    print("Addition of ",x,"+",y,"=",sum,end=" ")
    print("\n")

    sub = obj.Substraction(x,y)
    print("substraction of ",x,"-",y,"=",sub,end=" ")
    print("\n")

    mul = obj.Multiplication(x,y)
    print("Multiplication of ",x,"*",y,"=",mul,end=" ")
    print("\n")


    div = obj.Division(x,y)
    print("Division of ",x,"/",y,"=",div,end=" ")
    print("\n")

if __name__ == "__main__":
    main()

