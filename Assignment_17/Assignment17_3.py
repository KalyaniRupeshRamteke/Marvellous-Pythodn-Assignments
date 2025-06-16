import schedule
import time

def DisplayMsg():
    print("Do Coding...")

def main():

    print("Inside automation script")
    schedule.every(30).minutes.do(DisplayMsg)    # register it  , canonical call function

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
