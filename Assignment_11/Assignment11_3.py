Sum = 0
def SUM_OF_DIGIT(no):
    global Sum
    if(no > 0):
        y = no%10   #given the reminder of division
        Sum = Sum + y
        no = no // 10  #given the quetiont
        SUM_OF_DIGIT(no)
    return Sum

def main():
    print("Enter the number for addition of digits:")
    a = int(input())
    ret = SUM_OF_DIGIT(a)
    print(ret)

if __name__ == "__main__":
    main()
        