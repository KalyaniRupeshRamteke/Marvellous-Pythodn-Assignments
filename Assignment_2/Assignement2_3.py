def factorial(no):
    fact = 1
    for x in range(no,0,-1) :
        fact = fact * x
    
    return fact

def main() : 
    print("enter the number for factorial : ")
    x = int(input())

    res = factorial(x)
    print("factorial nmber is : ",res)

if __name__ == "__main__" :
    main()