import schedule
import datetime
import time

def writeCurrentTime():

    fobj = open("Marvellous.txt","a")
    currentTime = str(datetime.datetime.now())
    fobj.write(currentTime)
    fobj.write("/n")

    fobj.close()

def main():

    schedule.every(2).minutes.do(writeCurrentTime)    # register it  , canonical call function

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()

