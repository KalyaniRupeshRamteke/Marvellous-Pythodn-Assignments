import sys
import psutil
import CreateLog



def displayInfoGivenProcess(processName):
    
    processInfoList = []
    for proc in psutil.process_iter():
        info = proc.as_dict(attrs=['name'])  #inbuild function as_dict for create dictionary
        if (info["name"] == processName):
            processInfoList.append(info)

    return processInfoList

def main():

    if(len(sys.argv) == 2):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This application is used to display running process information.")
            print("This is the file automation script")
        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Used the given script as ")
            print("ScriptName.py processname")
            print("Please provide valid process name.")
        else:
            processName = sys.argv[1]
            runningProcInfo = displayInfoGivenProcess(processName)
            CreateLog.createLogFile("LogDirectoryAssignement21_2",runningProcInfo)
    else:
        print("Invalid number of arguments")
        print("Used the given flaga as:")
        print("--h : Used to disaplay the help.")
        print("--u : Used to disaplay the usage.")



if __name__ == "__main__":
    main()
    

