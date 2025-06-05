
def rightTriangle(no,counter):

    if(counter <  no):
        for  x in range(counter):
            print ("*",end=" ")
        print("\n")
        counter =  counter + 1
        rightTriangle(no,counter)

def main():
    rightTriangle(5,1)

if __name__ == "__main__":
    main()
