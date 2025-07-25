
import pandas as pd 
import DataFrameModule

def dataframeInfo():
    
    df = DataFrameModule.getDataFrame()

    print("Basic Information of Data")
    print("Diamention of data is :",df.shape)
    print("columns name is :",df.columns)
    print("Datatpes ",df.dtypes)
    print("Datatype of columns are : ")
    print(df['Name'].dtype)
    print(df['Math'].dtype)
    print(df['Science'].dtype)
    print(df['English'].dtype)

def main():
    dataframeInfo()

if __name__ == "__main__":
    main()