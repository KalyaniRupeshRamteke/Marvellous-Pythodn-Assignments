rev  = lambda x : x == reversed(x)

def main():
    print("Enter String")
    inputStr = input()

    res = rev(inputStr)

    if(res) :
        print(inputStr," is palimdrom")
    else:
        print(inputStr," is not palimdrom")
if __name__ == "__main__":
    main()



