def prime(x,y):
    for x in range(y):
        if( x % y)




def main():

    print("Enter number of elements:")
    num = int(input())
    print("Enter numric values:")
    data = []
    for i in range(num):
        data.append(int(input()))

    Mdata = list(map(doub,data))
    print("Map data is : ")
    print(Mdata)

if __name__ == "__main__":
    main()

    