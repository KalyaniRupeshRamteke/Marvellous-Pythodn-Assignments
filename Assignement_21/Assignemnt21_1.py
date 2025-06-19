import psutil
import CreateLog

def processInfo():

    processInfoList = []
    for proc in psutil.process_iter():
        info = proc.as_dict(attrs=['pid','name','username'])  #inbuild function as_dict for create dictionary
        processInfoList.append(info)

    return processInfoList


def main():
    processInformation = processInfo()
    CreateLog.createLogFile("LogDirectoryAssignmentt21_1",processInformation)

if  __name__ == "__main__":
    main()


