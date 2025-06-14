import os
def main():
    print("Enter file to create")
    filename = input()

    flag = os.path.exists(filename)
    if(flag == False):
        print("Enter valid file name.")
        exit()

    fobj = open(filename,"r")

    fobj1 = open("New.txt","w")

    lines = fobj.readlines()

    for line in lines:
        if line.strip() == "":
            continue
        else:
            fobj1.write(line)

    fobj.close()
    fobj.close()

if __name__ =="__main__":
    main()
