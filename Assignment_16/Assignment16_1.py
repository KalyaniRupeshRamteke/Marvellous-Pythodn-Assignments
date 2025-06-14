def main():

    fobj = open("Student.txt","w")

    print("Enter name of students:")
    for x in range(5):
        a = str(x) +"."+input()
        fobj.write(a)
        fobj.write("\n")

    fobj.close()


if __name__ == "__main__":
    main()