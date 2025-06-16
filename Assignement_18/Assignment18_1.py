import os
def main():
    print("Enter fine  name for check is exist in current directory or not?")
    fileName = input()

    flag = os.path.exists(fileName)

    if(flag == True):
        print(fileName ,"is exist",end=" ")
    else:
        print(fileName ,"is not exist",end=" ")



if __name__ == "__main__":
    main()