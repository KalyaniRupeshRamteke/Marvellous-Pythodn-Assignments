import os
import time

def createLogFile(folderName, data):

    flag = os.path.exists(folderName)
    
    if(flag == False):
        os.mkdir(folderName)
    
    timestamp = time.ctime()
    timestamp = timestamp.replace(" ","")
    timestamp = timestamp.replace(":","_")
    timestamp = timestamp.replace("/","_")

    filename = os.path.join(folderName,"Marvellous%s.log" %timestamp)
    fobj = open(filename,"w")
    border = "-"*80
    fobj.write(border)
    fobj.write("\n\t\tMarvellous Info system process log\n")
    fobj.write("\t\tLog file is created at:"+time.ctime()+"\n")
    fobj.write(border)
    fobj.write("\n")
    
    for x in data:
        fobj.write("%s \n" %x)

    fobj.write(border)
    fobj.close()

def generateLogFile(folderName, data):

    flag = os.path.exists(folderName)
    
    if(flag == False):
        os.mkdir(folderName)
    
    timestamp = time.ctime()
    timestamp = timestamp.replace(" ","")
    timestamp = timestamp.replace(":","_")
    timestamp = timestamp.replace("/","_")

    name = "Marvellous%s.log" %timestamp
    filename = os.path.join(folderName,"Marvellous%s.log" %timestamp)
    fobj = open(filename,"w")
    border = "-"*80
    fobj.write(border)
    fobj.write("\n\t\tMarvellous Info system process log\n")
    fobj.write("\t\tLog file is created at:"+time.ctime()+"\n")
    fobj.write(border)
    fobj.write("\n")
    
    for x in data:
        fobj.write("%s \n" %x)

    fobj.write(border)
    fobj.close()

    fileInfo = {"name": name,"path": filename}

    return fileInfo

