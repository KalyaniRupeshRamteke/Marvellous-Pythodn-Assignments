import os
import sys

def main():

    if(len(sys.argv) == 2):

        if(sys.argv[1] == "--h" or sys.argv == "--H"):
            print("This script is use for calcule frequncy of word in file.")
        elif (sys.argv[1] == "--u" or sys.argv == "--U"):
            print("Used the given script as ")
            print("ScriptNaem.py Argument1 Argument2")
        else:
            print("Invalid number of arguments")
            print("Used the given flag as:")
            print("--h : Used to disaplay the help.")
            print("--u : Used to disaplay the usage.")
    elif(len(sys.argv) == 3):
        filename = sys.argv[1]
        inputWord = sys.argv[2]

        flag = os.path.exists(filename)

        if(flag == False):
            print("Enter valid name of file")
            exit()
        
        fobj = open(filename,"r")

        counter = 0

        linesInFile= fobj.readlines()

        for x in linesInFile: 
            for word in x.split():
                if(inputWord == word):
                    counter = counter +1

        fobj.close()

        print(inputWord,": total count is",counter,"in",filename,end=" ")
    else:
        print("Invalid number of arguments")
        print("Used the given flag as:")
        print("--h : Used to disaplay the help.")
        print("--u : Used to disaplay the usage.")

if __name__ == "__main__":
    main()
