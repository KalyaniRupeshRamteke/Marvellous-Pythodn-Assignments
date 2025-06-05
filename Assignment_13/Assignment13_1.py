class BookStore:
    NoOfBooks = 0

    def __init__(self,name,author):
        BookStore.NoOfBooks = BookStore.NoOfBooks + 1
        self.Name = name
        self.Author=author

    def Display(self):
        #print("Sr.No:",BookStore.NoOfBooks)
        #print("Name of book",self.Name)
        #print("Author of book",self.Author)
        print(BookStore.NoOfBooks ,".",self.Name,"==>",self.Author,end=" ")
        print("\n")


def main():
    obj = BookStore("Linux System Programming","Robert Love")
    obj.Display()

    obj1 = BookStore("C programming","Dennis Ritchie")
    obj1.Display()

if __name__ == "__main__":
    main()
