
import pandas as pd 
import DataFrameModule

def dataDescription():

    df = DataFrameModule.getDataFrame()
    df.drop(columns = ['English'] , inplace = True)
    print("Drop col english")
    print(df.head())

def main():
    dataDescription()


if __name__ == "__main__":
    main()