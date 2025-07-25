import sys
import os
import CreateLog



def showFileNameAccExtention(dictName,extention):
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

    fileNameList = []
    for folderName,SubFolderNam,fileName in os.walk(dictName):
        for file in fileName:
            if(file.endswith(extention)):
                fileNameList.append(file)
    
    return fileNameList

def main():

    Border = "-"*80
    print(Border)
    print("--------------Marvellous-------------------")
    print(Border)

    if(len(sys.argv) == 2):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This application is used to display file name according to given extention by user.")
            print("This is the file automation script")
        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Used the given script as ")
            print("ScriptName.py nameOfDirectory nameOfFileExtention")
            print("Please provide valid absoulte path.")
        else:
            print("Invalid number of arguments")
            print("Used the given flaga as:")
            print("--h : Used to disaplay the help.")
            print("--u : Used to disaplay the usage.")
    elif(len(sys.argv) == 3):
        directoryName = sys.argv[1]
        fileExtention = sys.argv[2]

        fileNameList = showFileNameAccExtention(directoryName,fileExtention)
        if(len(fileNameList) > 0):
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
    

