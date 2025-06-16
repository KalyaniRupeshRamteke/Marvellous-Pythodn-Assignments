import schedule
import time
import datetime

def DisplayCurrentTime():
    print(datetime.datetime.now())

def main():

    print("Inside automation script")
    schedule.every(1).minute.do(DisplayCurrentTime)    # register it  , canonical call function

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
