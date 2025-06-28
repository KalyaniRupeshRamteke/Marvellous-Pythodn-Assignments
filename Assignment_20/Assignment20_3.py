import hashlib
import os
import sys
import CreateLog

def checkSumFile(filename,blockSize):

    fobj = open(filename,"rb")

    hobj = hashlib.md5()
    buffer = fobj.read(blockSize)
    while(len(buffer)>0):
        hobj.update(buffer)
        buffer =fobj.read()

    fobj.close()

    return hobj.hexdigest()

def checkSumOfAllFilesOfDict(dictName):

    flag = os.path.isabs(dictName)

    if(flag == False):
        dictName = os.path.abspath(dictName)
    
    flag = os.path.exists(dictName)

    if(flag == False):
        print("Path is invalid")

    flag = os.path.isdir(dictName)

    if(flag == False):
        print("Path is valid but target is not directory")

    checkSumFileList = {}

    for folderName,subFolderNames,fileNames in os.walk(dictName):

        for filename in fileNames :
            filename = os.path.join(folderName,filename)
            checksum = checkSumFile(filename,1024)
            if checksum in checkSumFileList:
                checkSumFileList[checksum].append(filename)
            else:
                checkSumFileList[checksum] = [filename]

    return checkSumFileList

def deleteduplicatefiles(MyDict):

    result = list(filter(lambda x : len(x) >1 ,MyDict.values()))

    x = []
    count = 0
    cnt = 0
    for value in result:
        for subvalue in value:
            count = count + 1
            if(count > 1):
                print("Delete files :", subvalue)
                x.append(subvalue)
                os.remove(subvalue)
                cnt = cnt + 1
        count = 0

    print("Total delete files", cnt)

    return x

def main():
    

    #Logic
    if(len(sys.argv) == 2):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This application is used to generate log file for duplicate files in dictonaty.")
            print("This is the File1 IO automation script")

        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Used the given script as ")
            print("ScriptName.py nameOfDirectory")
            print("Please provide valid absoulte path.")
        else:
            dictName = sys.argv[1]
            checkSumInfo = checkSumOfAllFilesOfDict(dictName)
            deletedlogfile = deleteduplicatefiles(checkSumInfo) 

            CreateLog.createLogFile("Assignment_20",deletedlogfile)

    else:
        print("Invalid number of arguments")
        print("Used the given flaga as:")
        print("--h : Used to disaplay the help.")
        print("--u : Used to disaplay the usage.")

if __name__ == "__main__":
    main()
