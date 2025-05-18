def factors(no) : 
    factSum = 0

    for i in range(1,no) :
        if(no % i == 0) : 
            factSum = factSum + i
    return factSum

def main() :
    print("Enter the number : ")
    num = int(input())

    res = factors(num)
    print("Addition of factors is : ",res)

if __name__ == "__main__":
    main()
