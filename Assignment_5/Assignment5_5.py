def main():
    print("Enter number")
    no = int(input())

    print("------------")
    if(no % 2 == 0):
        print(no," is even")
    else:
        print(no," is odd")

if __name__ =="__main__":
    main()