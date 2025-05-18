#define the fuction for return  frequncy of number from user input list
def frqNum(inputdata,numSearch):
    cnt = 0
    for no in range(len(inputdata)):
        if(inputdata[no] == numSearch) :
            cnt = cnt+1
    
    return cnt


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

    print("Element to search")
    searchNumber = int(input())

    res = frqNum(data,searchNumber)

    print("Frequency of number is  : ",res)

if __name__ == "__main__":
    main()
    