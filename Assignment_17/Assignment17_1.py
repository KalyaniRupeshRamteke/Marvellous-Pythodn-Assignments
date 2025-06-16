import schedule
import time

def display():
    print("Test sheduler......")

def main():

    print("Inside automation script")
    schedule.every(2).seconds.do(display)    # register it  , canonical call function

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
