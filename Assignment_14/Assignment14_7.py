class Person:

    def __init__(self,name,age):
        self.Name= name
        self.Age = age

class Teacher(Person):

    def __init__(self,sub,sal,name,age):
        self.Subject =sub
        self.Salary = sal
        super().__init__(name,age)

    def Display(self):
        print("Name:",self.Name)
        print("Age:",self.Age)
        print("Subject",self.Subject)
        print("Salary",self.Salary)

def main():

    obj = Teacher("Mathmatics",10000,"Kalyani",35)

    obj.Display()

if __name__ == "__main__":
    main()


