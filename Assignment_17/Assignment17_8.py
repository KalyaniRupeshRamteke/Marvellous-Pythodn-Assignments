import schedule
import time

def mailInboxUpdateChk():
    print("Checking mail...")


def main():

    schedule.every(10).seconds.do(mailInboxUpdateChk)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()

