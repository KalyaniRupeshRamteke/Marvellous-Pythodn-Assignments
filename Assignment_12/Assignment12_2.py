class Circle:
    PI =  3.14
    def __init__(self):
        self.Radius =0.0
        self.Area = 0.0
        self.circumferance = 0.0

    def Accept(self,r):
        self.Radius = r

    def calculateArea(self):
        self.Area = self.Radius * self.Radius * Circle.PI

    def calculateCircumfarance(self):
        self.circumferance = 2 * Circle.PI * self.Radius

    def Display(self):
        print("Radius of circle is :",self.Radius)
        print("Area of circle is : ",self.Area)
        print("Area of circumferance is :",self.circumferance)
    
def main():

    print("Enter radius of circle")
    a = int(input())

    cir = Circle()
    cir.Accept(a)
    cir.calculateArea()
    cir.calculateCircumfarance()
    cir.Display()
    
    print("Enter radius of circle")
    b = int(input())

    cir1 = Circle()
    cir1.Accept(b)
    cir1.calculateArea()
    cir1.calculateCircumfarance()
    cir1.Display()
    

if __name__ == "__main__":
    main()



