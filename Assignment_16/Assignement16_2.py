import os
def main():
    print("Enter the file name for reading:")
    filename = input()

    flag = os.path.exists(filename)
    if(flag == False):
        print("Please enter valid file name")
        exit()

    fobj = open(filename,"r")
    
    data = fobj.read()

    print("File contents are as follows")
    print(data)

    fobj.close()

if __name__ == "__main__":
    main()