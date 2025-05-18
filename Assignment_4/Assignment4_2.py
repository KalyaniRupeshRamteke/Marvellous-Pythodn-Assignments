mult = lambda a,b : a*b

def main():
    print("Enter first number:")
    no1 = int(input())

    print("Enter Second number:")
    no2 = int(input())

    result = mult(no1,no2)

    print("Power of number is",result)

if __name__ == "__main__":
    main()