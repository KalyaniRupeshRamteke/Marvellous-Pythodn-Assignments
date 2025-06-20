import os
import MyCheckSum
import CreateLog
import sendMail
import schedule
import sys
import time

def CheckDuplicateFiles(dictName):
    flag = os.path.isabs(dictName)
    
    if(flag == False):
        dictName = os.path.abspath(dictName)
    
    flag = os.path.exists(dictName)

    if(flag == False):
        print("Please enter valid name of directory")
        exit()

    duplicate = {}
    totalNumScanned = 0

    for folderName , subFolderNames, fileNames in os.walk(dictName):

        for fname in fileNames:
            fname = os.path.join(folderName,fname)
            totalNumScanned = totalNumScanned+1
            chekSumVal = MyCheckSum.calculateCheckSum(fname)
            if chekSumVal in duplicate:
                duplicate[chekSumVal].append(fname)
            else:
                duplicate[chekSumVal] = [fname]

    return duplicate,totalNumScanned

def deleteDuplicateFile(path,mailId):

    timestamp = time.ctime()

    resultArr,totalCnt=CheckDuplicateFiles(path)

    result = list(filter(lambda x : len(x) > 0 , resultArr.values()))

    delFileNameList = []
    deleteFileCnt = 0
    checkSumCnt = 0
    for value in result:
        for subValue in value:
            checkSumCnt = checkSumCnt+1
            if(checkSumCnt>1):
                print(subValue)
                delFileNameList.append(subValue)
                os.remove(subValue)
                deleteFileCnt = deleteFileCnt +1
            
        checkSumCnt =0

    #info ={}
    #info = {"TotalFileScan" : totalNumScanned , "TotalFileDelete" : deleteFileCnt}


    #Log file function
    fileInfo = CreateLog.generateLogFile("Marvellous",delFileNameList)

    #Send MAil
    mailbody = "Starting time of scanning"+timestamp+"\n Total Files scanned:"+str(totalCnt)+"\n Total number of duplicateFile found :" +str(deleteFileCnt)

    mailInfo = {"subject": "Duplicate file(s) delete log","body": mailbody}
    sendMail.sendMailWithAttachment(mailId,fileInfo,mailInfo)
def main():
    
    Border  = "_"*54
    print(Border)
    print("------------Masrvelloud Automation----------------")
    print(Border)

    #Logic
    if(len(sys.argv) == 2):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This application is used to perform directory cleaning.")
            print("This is the directory automation script")

        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Used the given script as ")
            print("ScriptNaem.py nameOfDirectory timeinterval mailId")
            print("Please provide valid absoulte path.")
        else:
            print("Invalid number of arguments")
            print("Used the given flaga as:")
            print("--h : Used to disaplay the help.")
            print("--u : Used to disaplay the usage.")


        
    elif(len(sys.argv) == 4):

        dictName = sys.argv[1]
        timeinterval = int(sys.argv[2])
        receiverMailId = sys.argv[3]

        schedule.every(timeinterval).minutes.do(deleteDuplicateFile,dictName,receiverMailId)        

        while True:
            schedule.run_pending()
            time.sleep(1)
    else:
        print("Invalid number of arguments")
        print("Used the given flaga as:")
        print("--h : Used to disaplay the help.")
        print("--u : Used to disaplay the usage.")


    print(Border)
    print("------------Marvellous Infosystem----------------")
    print(Border)

if __name__ == "__main__":
    main()






            
