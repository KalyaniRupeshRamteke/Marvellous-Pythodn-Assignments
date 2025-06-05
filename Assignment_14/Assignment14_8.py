class Vehicle:

    def start(self):
        print("In base class method")

class Car(Vehicle):

    def start(self):
        print("In derive class start")


def main():

    obj = Car()

    obj.start()

if __name__ == "__main__":
    main()