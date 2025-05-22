def main():
    print("Enter temprature in celsius : ")
    temp = int(input())
    
    F = (temp * (9/5)) + 32

    print("Temprature in Fahrenheit : ",F)

if __name__ == "__main__":
    main()