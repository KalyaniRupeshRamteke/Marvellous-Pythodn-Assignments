def Add(no1,no2) :
    ans = 0
    ans = no1+no2
    return ans

def Sub(no1,no2):
    ans = 0
    if(no2>no1):
        ans = no2-no1
    else:
        ans = no1-no2
    return ans

def Mul(no1,no2):
    ans = 0
    ans = no1 * no2
    return ans

def Div(no1,no2) :
    ans = 0
    if(no2 != 0):
        ans = no1/no2
    elif(no1 != 0):
        ans = no2 / no1
    return ans