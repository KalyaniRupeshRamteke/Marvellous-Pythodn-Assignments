def main():

    print("Enter size of number")
    size = int(input())

    fobj = open("Numbers.txt","w")

    for x in range(size):
        fobj.write(input())
        fobj.write("\n")

    fobj.close()

if __name__ == "__main__":
    main()