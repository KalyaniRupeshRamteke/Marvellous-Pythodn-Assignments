
import pandas as pd 
import DataFrameModule

def changeNameValue():

    df = DataFrameModule.getDataFrame()
    print(df.head())
    print("Get udated data:")

    df['Name'].replace('Pooja', 'Puja', inplace=True) 
    print(df.head())


def main():
    changeNameValue()

if __name__ == "__main__":
    main()