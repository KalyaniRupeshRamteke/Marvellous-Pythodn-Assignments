sum = 0
def sum_of_nat_number(no):
    global sum
    if(no > 0):
        sum = sum + no
        no = no - 1
        sum_of_nat_number(no)
    return sum

def main():
    print("Enter the number for addition of natural numbers:")
    a = int(input())
    ret = sum_of_nat_number(a)
    print(ret)
if __name__ == "__main__":
    main()