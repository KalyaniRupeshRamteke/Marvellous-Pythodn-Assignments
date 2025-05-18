from functools import reduce

evenNum = lambda val : (val % 2 == 0) 
sqrEven = lambda b : (b*b)
listAdd = lambda b,a : (b+a)

def main() :
    print("Enter size of elements : ")
    size =int(input())

    inputData = []

    for i in range(size):
        inputData.append(int(input()))

    FData = list(filter(evenNum,inputData))
    print("Filter data is:",FData)

    MData = list(map(sqrEven,FData))
    print("Map data is:",MData)

    RData = reduce(listAdd,MData)
    print("Reduce is :",RData)

if __name__ == "__main__":
    main()