from functools import reduce

def prime(val) :
    ans = True
    i = 2
    while (i < val) :
        if(val % i == 0):
            ans = False
            break
        i = i+1

    if(ans == True) :
        return ans

def multiplication(val):
    mult = val * 2
    return mult

def maxNumer(val1,val2):
    if(val1 < val2):
        return val2
    else:
        return val1


def main() :
    print("Enter size of elements : ")
    size =int(input())

    inputData = []

    for i in range(size):
        inputData.append(int(input()))

    FData = list(filter(prime,inputData))
    print("Filter data is:",FData)

    MData = list(map(multiplication,FData))
    print("Map data is:",MData)

    RData = reduce(maxNumer,MData)
    print("Reduce is :",RData)

if __name__ == "__main__":
    main()