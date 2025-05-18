#define the fuction for return  minimum  number from all ements in list
def minNum(inputdata):
    min = inputdata[0]
    for no in range(len(inputdata)):
        if(inputdata[no] < min) :
            min = inputdata[no]
    
    return min


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
        
    res = minNum(data)

    print("Minimum number fromm all elements in list is : ",res)

if __name__ == "__main__":
    main()
    