import MarvellousNum

#define the fuction for return  addition of all prime number in list
def ListPrime(inputdata):
    sum = 0
    for no in range(len(inputdata)):
        ans = MarvellousNum.chkPrime(inputdata[no])
        if(ans == True) :
            sum = sum+inputdata[no]
    
    return sum


def main() :
    #Accept size of elements from user
    print("Enter elements number")
    size = int(input())

    #declare empty list name of data
    data = []

    print("Enter numeric value")
    #iterate for loop yo accept input from user for size of elements
    for x in range(size):
        ele = int(input())
        #append the number in list
        data.append(ele)



    #print the data list which accept from user
    print(data)

    res = ListPrime(data)

    print("Frequency of prime number is  : ",res)

if __name__ == "__main__":
    main()
    