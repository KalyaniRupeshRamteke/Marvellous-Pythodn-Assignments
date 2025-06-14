import os
def main():
    print("Enter the file which you want ro read")
    filename = input()

    flag = os.path.exists(filename)

    if(flag == False):
        print("please enter valid name of file")
        exit()
    

    fobj = open(filename,"r")
    data = fobj.read()

    print("File contens are as follows")
    print(data)

    fobj.close()

if __name__ == "__main__":
    main()