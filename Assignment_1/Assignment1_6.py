def NumberPositiveNegative(no) :
    if(no == 0) :
        print("Zero")
    elif(no < 0) :
        print("Negative")
    else :
        print("Positive")
def main() :   
    print("Enter  one number")
    val = int(input())

    NumberPositiveNegative(val)

if __name__ == "__main__" :
    main()