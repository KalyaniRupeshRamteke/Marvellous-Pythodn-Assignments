
import pandas as pd 
import DataFrameModule

def addTotalCol():

    df = DataFrameModule.getDataFrame()
    print("Add Total Col in dataframe")

    df.insert(4, 'Total', df['Math'] + df['Science'] + df['English']) # index 1, column name, values


    print(df.head())

def main():
    addTotalCol()

if __name__ == "__main__":
    main()