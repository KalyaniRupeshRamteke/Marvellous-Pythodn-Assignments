from functools import reduce

def main():

    print("Enter number of elements:")
    num = int(input())
    print("Enter numric values:")
    data = []
    for i in range(num):
        data.append(int(input()))

    RData = reduce(lambda a,b : a*b ,data)
    print("Reduce data is : ")
    print(RData)

if __name__ == "__main__":
    main()

    