class Demo:
    value = "Clss Variable"
    def __init__(self,a,b):
        self.no1 = a
        self.no2 = b

    def fun(self):
        print("The value of no1 variable is : ",self.no1)
    
    def gun(self):
        print("The value of no2 variable is : ",self.no2)

def main():
    obj1 = Demo(11,21)
    obj2 = Demo(51,101)

    obj1.fun()
    obj2.fun()

    obj1.gun()
    obj2.gun()

if __name__ == "__main__":
    main()