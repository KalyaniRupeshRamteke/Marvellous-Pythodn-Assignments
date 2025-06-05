class Product:

    def __init__(self,name,price):
        self.Name = name
        self.Price = price

def __eq__(a,b):
    if(a.Price == b.Price):
        print(a.Name ,"and",b.Name,"price are same",end=" ")
    else:
        print(a.Name ,"and",b.Name,"price are not same",end=" ")
    print("\n
    ")

def main():

    product1 = Product("LCD",10000)
    product2 = Product("Mouse",750)

    __eq__(product1,product2)

    product1 = Product("HP Laptop Elite book",5000)
    product2 = Product("HP Laptop",5000)

    __eq__(product1,product2)


if __name__ == "__main__":
    main()