import multiprocessing

def square(no):
    result = 0
    result = no * no
    return result

def main():

    print("Enter size of data")
    size = int(input())

    data=[]

    print("Enter numric values")

    for x in range(size):
        data.append(int(input()))

    p = multiprocessing.Pool()
    mData =[]

    mData = p.map(square,data)
    p.close()
    p.join()

    print(mData)

if __name__ == "__main__":
    main()