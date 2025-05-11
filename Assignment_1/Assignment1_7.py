def DivisibleByFive(no) :
    if(no%5 == 0) :
        return True
    else:
        return False

def main() :
    print("Enter one number")
    val = int(input())

    result = DivisibleByFive(val)

    print(result)


if __name__ == "__main__" : 
    main()