import pandas as pd 
def main():

    data = {'Name':['A','B','C'],'Age':[21.0,22.0,23.00]}
    df = pd.DataFrame(data)

    print("DataType of Age col:")
    print(df['Age'].dtype)

    print("Data after chage data type of Age col as int:")
    df['Age'] = df['Age'].astype(int)
    print(df)

    

    
if __name__ == "__main__":
    main()