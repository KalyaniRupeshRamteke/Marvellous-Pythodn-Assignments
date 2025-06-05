class Book:

    def __init__(self):
        self.__price=0

    def set(self,price):
        self.__price = price
    
    def get(self):
        return self.__price

def main():
    obj = Book()

    obj.set(100)

    price = obj.get()
    print("Price of book is",price)

if __name__ == "__main__":
    main()