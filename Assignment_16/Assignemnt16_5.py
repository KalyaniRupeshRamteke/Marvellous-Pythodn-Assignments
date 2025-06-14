import os

def main():

    print("Enter the file to read:")
    filename = input()

    flag = os.path.exists(filename)
    if(flag == False):
        print("enter valid file name")
        exit()

    fobj = open(filename,"r")

    counter = 0

    linesInFile= fobj.readlines()

    for x in linesInFile: 
        counter = 0
        for word in x.split():
            counter = counter +1
            if(counter>5):
                print(x)
                break

    fobj.close()

if __name__ == "__main__":
    main()
