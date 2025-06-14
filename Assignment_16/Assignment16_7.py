import os
def main():

    print("Enter file name to read")
    filename = input()

    flag = os.path.exists(filename)

    if(flag == False):
        print("Please  enter valid name of file.")
        exit()

    fobj = open(filename,"r")

    lines = fobj.readlines()

    for line in lines:
        for word in line.split():
            if(word.isnumeric() == False):
                nameOfStudent = word
            if(word.isnumeric() == True and int(word) > 75):
                print(nameOfStudent)

    fobj.close()

if __name__ == "__main__":
    main()