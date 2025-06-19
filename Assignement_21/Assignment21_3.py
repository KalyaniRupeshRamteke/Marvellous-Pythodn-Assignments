import sys
import psutil
import CreateLog



def processInfo():
    
    processInfoList = []
    for proc in psutil.process_iter():
        info = proc.as_dict(attrs=['pid','name','username'])  #inbuild function as_dict for create dictionary
        processInfoList.append(info)

    return processInfoList

def main():

    if(len(sys.argv) == 2):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This application is used to create log file in directory taking input from  user.")
            print("This is the file automation script")
        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Used the given script as ")
            print("ScriptName.py directoryName")
            print("Please provide valid process name.")
        else:
            directoryName = sys.argv[1]
            runningProcInfo = processInfo()
            CreateLog.createLogFile(directoryName,runningProcInfo)
    else:
        print("Invalid number of arguments")
        print("Used the given flaga as:")
        print("--h : Used to disaplay the help.")
        print("--u : Used to disaplay the usage.")



if __name__ == "__main__":
    main()
    

