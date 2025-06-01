from functools import reduce

greaterNum = lambda val : (70 <= val and val <= 90) 
addTen = lambda b : (int(b)+10)
listMult = lambda b,a : (b*a)

def main() :
    print("Enter size of elements : ")
    size =int(input())

    inputData = []

    for i in range(size):
        inputData.append(int(input()))

    FData = list(filter(greaterNum,inputData))
    print("Filter data is:",FData)

    MData = list(map(addTen,FData))
    print("Map data is:",MData)

    RData = reduce(listMult,MData)
    print("Reduce is :",RData)

if __name__ == "__main__":
    main()