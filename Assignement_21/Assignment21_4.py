import sys
import psutil
import CreateLog
import sendMail



def processInfo():
    
    processInfoList = []
    for proc in psutil.process_iter():
        info = proc.as_dict(attrs=['pid','name','username'])  #inbuild function as_dict for create dictionary
        processInfoList.append(info)

    return processInfoList

def main():

    if(len(sys.argv) == 2):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This application is used to create log file in directory taking input from  user & send mail with attachment")
            print("This is the file automation script")
        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Used the given script as ")
            print("ScriptName.py directoryName mailId")
            print("Please provide valid process name.")
        else:
            print("Invalid number of arguments")
            print("Used the given flaga as:")
            print("--h : Used to disaplay the help.")
            print("--u : Used to disaplay the usage.")

    elif(len(sys.argv) == 3):
        
        directoryName = sys.argv[1]
        mailId = sys.argv[2]

        runningProcInfo = processInfo()
        fileInfo = CreateLog.generateLogFile(directoryName,runningProcInfo)
        mailInfo = {"subject": "Runing Process Information","body": "Please Find attachement"}
        sendMail.sendMailWithAttachment(mailId,fileInfo,mailInfo)


    else:
        print("Invalid number of arguments")
        print("Used the given flaga as:")
        print("--h : Used to disaplay the help.")
        print("--u : Used to disaplay the usage.")



if __name__ == "__main__":
    main()
    

