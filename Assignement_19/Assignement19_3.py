import sys
import os
import CreateLog



def copyFiles(dictName,destDir):
    flag = os.path.isabs(dictName)

    if(flag == False):
        dictName = os.path.abspath(dictName)

    flag = os.path.exists(dictName)
    if(flag == False):
        print("Path is invalid")
        return

    flag = os.path.isdir(dictName)
    if(flag == False):
        print("Invalid directory name")
        return

    os.mkdir(destDir)
    
    fileNameList = []
    for folderName,SubFolderNam,fileName in os.walk(dictName):
        for file in fileName:
            name = os.path.join(destDir,file)
            sFName = os.path.join(folderName,file) #source file full path
            fobj = open(name,"w")
            sFobj = open(sFName,"r")
            data = sFobj.read()
            fobj.write(data)
            sFobj.close()
            fobj.close()
            fileNameList.append(name)
    
    return fileNameList

def main():

    Border = "-"*80
    print(Border)
    print("--------------Marvellous-------------------")
    print(Border)

    if(len(sys.argv) == 2):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This application is used to copy files in new directory.")
            print("This is the file automation script")
        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Used the given script as ")
            print("ScriptName.py sourceDirectory destDirectory")
            print("Please provide valid absoulte path.")
        else:
            print("Invalid number of arguments")
            print("Used the given flaga as:")
            print("--h : Used to disaplay the help.")
            print("--u : Used to disaplay the usage.")
    elif(len(sys.argv) == 3):
        sourceDir = sys.argv[1]
        destDir = sys.argv[2]

        fileNameList = copyFiles(sourceDir,destDir)
        CreateLog.createLogFile("FileAutomationLogs",fileNameList)
    else:
        print("Invalid number of arguments")
        print("Used the given flaga as:")
        print("--h : Used to disaplay the help.")
        print("--u : Used to disaplay the usage.")

    print(Border)
    print("--------------Marvellous-------------------")
    print(Border)


if __name__ == "__main__":
    main()
    

