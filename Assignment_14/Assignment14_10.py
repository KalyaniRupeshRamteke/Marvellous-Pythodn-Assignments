class Employee:

    def __init__(self,name,Salary,dept):
        self.Name = name
        self.__Salary = Salary
        self._department = dept 

    def Display(self):
        print("Name: ",self.Name)
        print("Salary: ",self.__Salary)
        print("Department: ",self._department)

def main():

    obj = Employee("Kalyani",4500,"Development")
    obj.Display()

    print(obj.Name)
    print(obj._department)
    #print(obj.__Salary) Given this error #AttributeError: 'Employee' object has no attribute '__Salary'
    


if __name__ == "__main__":
    main()
