class Employee:

    def __init__(self,name,id,salary):
        self.Name = name
        self.Emp_id = id
        self.Salary = salary

    def Display(self):
        print("Name",self.Name)
        print("ID",self.Emp_id)
        print("Salary",self.Salary)

def main():

    obj = Employee("Rohit",101,5000)
    obj.Display()

if __name__ == "__main__":
    main()