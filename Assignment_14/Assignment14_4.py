class Student:
    school_name ="ABC"

    def __init__(self,name,rollNo):
        self.Name = name
        self.rollNo = rollNo

    def Display(self):
        print("Name of student is:",self.Name)
        print("Roll number of student is :",self.rollNo)
        print("School name is",Student.school_name)

def main():

    obj = Student("Kalyani",101)

    print("Initially")
    obj.Display()
    Student.school_name = "MNO"
    print("After changing class name")
    obj.Display()

if __name__ == "__main__":
    main()
