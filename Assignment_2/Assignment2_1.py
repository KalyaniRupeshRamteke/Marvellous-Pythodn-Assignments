import Arithmatic

def main() :
    print("Please Enter 2 Number for mathamatical operations: ")
    val1 = int(input())
    val2 = int(input())

    addition = Arithmatic.Add(val1,val2)
    print("Adition is : ",addition)

    substraction =Arithmatic.Sub(val1,val2)
    print("Substraction is : ",substraction)

    multiplication = Arithmatic.Mul(val1,val2)
    print("Multiplication is : ",multiplication)

    division = Arithmatic.Div(val1,val2)
    print("Division is : ",division)

if __name__ == "__main__" :
    main()