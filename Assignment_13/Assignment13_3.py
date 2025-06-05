class Numbers:
    def __init__(self,a):
        self.Value = a 

    def chkPrime(self):
        
        ans = True
        i = 2
        while (i < self.Value) :
            if(self.Value % i == 0):
                ans = False
                break
            i = i+1
        if(ans == True):
            return "Prime number"
        else:
            return "Not prime number"

    def checkperfect(self):
        sum = self.sumfactor()
        if(sum == self.Value):
            return "Perfect number"
        else:
            return "Not perfect number"

    def sumfactor(self):
        sum = 0 
        i=1
        while(i < self.Value):
            if(self.Value%i == 0):
                sum = sum + i 
            i = i+1
        return sum
    
    def factors(self):
        factorslist = []
        i=1
        while(i < self.Value):
            if(self.Value%i == 0):
                factorslist.append(i)
            i = i+1
        return factorslist

def main():

    print("Enter the number")
    a = int(input())

    obj1= Numbers(a)
    ret = obj1.chkPrime()
    print(a,"is",ret,end=" ")
    print("\n")

    ret = obj1.checkperfect()
    print(a,"is",ret,end=" ")
    print("\n")

    ret = obj1.sumfactor()
    print("sum of Factors is :  ",ret,end=" ")
    print("\n")

    ret = obj1.factors()
    print("Factor list is:",ret,end=" ")
    print("\n")

if __name__ == "__main__":
    main()

