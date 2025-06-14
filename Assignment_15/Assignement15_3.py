import os
import sys
def main():

    if(len(sys.argv) == 2):

        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This program is use for copy one data from another file.")
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Used the given script as ")
            print("ScriptNaem.py Argument1")
        else:
            filename = sys.argv[1]
            flag = os.path.exists(filename)
            if(flag == False):
                print("enter valid name of file name to write data to Demo1.txt file")
                exit()

            fobj = open("Demo3.txt","w")

            fobj2 = open(sys.argv[1],"r")
            data = fobj2.read()

            fobj.write(data)

            fobj.close()
            fobj2.close()
            
    else:
        print("Invalid number of arguments")
        print("Used the given flaga as:")
        print("--h : Used to disaplay the help.")
        print("--u : Used to disaplay the usage.")
            

if __name__ == "__main__":
    main()