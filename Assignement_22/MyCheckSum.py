import hashlib  #use to calculate checksum of file

def calculateCheckSum(path,blockSize=1024):

    fobj = open(path,"rb") #file read in binary mode

    hobj = hashlib.md5() #hashlib module has class md5
    
    buffer = fobj.read(blockSize)  #10124 byte = 1 kb
    while(len(buffer) > 0):
        hobj.update(buffer)
        buffer = fobj.read(blockSize)        

    fobj.close()

    return hobj.hexdigest()  #calculate checksum bu using hexdigest() meyhod