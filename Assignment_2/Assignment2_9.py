def main() :
    print("Enter number")
    x = int(input())

    print("-------------")
    count = 0
    while(x > 0):
        count = count+1
       # print(x)
        x = x//10

    print("The digits of number is : ",count)

if __name__ == "__main__" :
    main()