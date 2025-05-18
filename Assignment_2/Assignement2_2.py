def main() :
    print("Enter size for print pattern : ")
    size = int(input())

    for x in range(size) : 
        i = 0
        while(i < size) :
            print ("*",end=' ')
            i = i +1
        print("\n")
    
if __name__ == "__main__":
    main()