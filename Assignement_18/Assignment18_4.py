import os
import sys

def main():

    if(len(sys.argv) == 2):

        if(sys.argv[1] == "--h" or sys.argv == "--H"):
            print("This script is use for compare two fils are content same data.")
        elif (sys.argv[1] == "--u" or sys.argv == "--U"):
            print("Used the given script as ")
            print("ScriptNaem.py Argument1 Argument2")
        else:
            print("Invalid number of arguments")
            print("Used the given flag as:")
            print("--h : Used to disaplay the help.")
            print("--u : Used to disaplay the usage.")
    elif(len(sys.argv) == 3) :
        filename1 = sys.argv[1]
        filename2 = sys.argv[2]

        flag = os.path.exists(filename1)

        if(flag == False):
            print(filename1, "no such file , please enter valid name." , end=" ")
            exit()

        flag = os.path.exists(filename2)
        if(flag == False):
            print(filename2, "no such file , please enter valid name." , end=" ")
            exit()

        fobj = open(filename1,"r")
        fobj1 = open(filename2,"r")

        data1 = fobj.read()
        data2 = fobj1.read()

        if(data1 == data2):
            print("Success")
        else:
            print("Failure")

        fobj.close()
        fobj1.close()

    else:
        print("Invalid number of arguments")
        print("Used the given flag as:")
        print("--h : Used to disaplay the help.")
        print("--u : Used to disaplay the usage.")

if __name__ == "__main__":
    main()