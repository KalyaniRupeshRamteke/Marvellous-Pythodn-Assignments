def main() :
    print("Enter first number")
    a = int(input())
    
    print("Enter second number")
    b = int(input())
    
    print("Enter third number")
    c = int(input())

    if(a > b) :
        if(a > c) :
            print("Largest value is",a)
        else:
            print("Largest value is ",c)
    elif(b > c):
        print("Largest value is ",b)
    else:
        print("Largest value is",c)

if __name__ == "__main__":
    main()
