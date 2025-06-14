import os
def main():
    print("Enter the file to write")
    filename = input()

    flag = os.path.exists(filename)

    if(flag == False):
        print("Enter valid file name")
        exit()

    fobj1= open("Destination.txt","w")
    fobj = open(filename,"r")

    sourceFileData = fobj.read()

    fobj1.write(sourceFileData)

    fobj.close()
    fobj1.close()

if __name__ == "__main__":
    main()
