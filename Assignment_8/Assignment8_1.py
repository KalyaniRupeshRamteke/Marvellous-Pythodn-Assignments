import threading

def chkEven(no):
    
    for x in range(no) : #here take 11 because of we have to print even number upto 10
        if(x % 2 ==0):
            print(x )


def chkOdd(no):
    for x in range(no) : 
        if(x % 2 != 0):
            print(x)


def main():
    even = threading.Thread(target = chkEven, args=(100,))
    odd = threading.Thread(target=chkOdd,args=(100,))

    print("Even Number is : ")
    even.start()
    print("Odd Number is : ")
    odd.start()

    even.join() # to wait main thread until even thread excution is end
    odd.join()

if __name__ == "__main__":
    main()
