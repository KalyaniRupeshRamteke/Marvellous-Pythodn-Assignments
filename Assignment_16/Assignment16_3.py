import os
def main():

    print("enter the file name to count line, words and characters:")
    filename = input()

    flag = os.path.exists(filename)

    if(flag == False):
        print("Enter valid file name")
        exit()

    fobj = open(filename,"r")

    lineCount = 0
    wordCount = 0
    characters = 0

    lines = fobj.readlines()

    for line in lines:
        lineCount = lineCount + 1
        for word in line.split():
            wordCount = wordCount+1
            for i in word:
                characters = characters +1

    fobj.close()

    print("Line number is:",lineCount)
    print("Word count is :", wordCount)
    print("character count is :",characters)

if __name__ == "__main__":
    main()
